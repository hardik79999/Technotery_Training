from flask import jsonify
from database import database

def get_dashboard_data_route(current_user):
    conn = None
    cursor = None
    try:
        conn = database()
        cursor = conn.cursor()

        users = []
        tasks = []
        admin_stats = {}
        chart_data = {'pending': 0, 'in progress': 0, 'completed': 0}

        # 📊 LIVE CHART CALCULATION (Power BI style)
        if current_user['role'] == 'admin':
            cursor.execute("SELECT status, COUNT(*) FROM tasks WHERE is_active = 1 GROUP BY status")
        elif current_user['role'] == 'manager':
            cursor.execute("SELECT status, COUNT(*) FROM tasks WHERE (assigned_by = %s OR assigned_to = %s) AND is_active = 1 GROUP BY status", (current_user['id'], current_user['id']))
        else:
            cursor.execute("SELECT status, COUNT(*) FROM tasks WHERE assigned_to = %s AND is_active = 1 GROUP BY status", (current_user['id'],))
        
        for row in cursor.fetchall():
            chart_data[row[0]] = row[1]

        # ==========================================
        # 👑 ADMIN LOGIC
        # ==========================================
        if current_user['role'] == 'admin':
            cursor.execute("""
                SELECT u1.uuid, u1.username, u1.role, IFNULL(u2.username, 'System') 
                FROM users u1 LEFT JOIN users u2 ON u1.created_by = u2.id WHERE u1.role != 'admin'
            """)
            users = [{"uuid": row[0], "username": row[1], "role": row[2], "creator": row[3]} for row in cursor.fetchall()]

            cursor.execute("SELECT COUNT(*) FROM users WHERE role = 'employee'")
            admin_stats['total_employees'] = cursor.fetchone()[0]

            cursor.execute("""
                SELECT t.uuid, t.title, t.description, t.status, IFNULL(u.username, 'Unassigned') as assigned_to,
                       DATE_FORMAT(t.created_at, '%d-%b-%Y %h:%i %p'), DATE_FORMAT(t.updated_at, '%d-%b-%Y %h:%i %p')
                FROM tasks t LEFT JOIN users u ON t.assigned_to = u.id WHERE t.is_active = 1
            """)
            tasks = [{"uuid": row[0], "title": row[1], "description": row[2], "status": row[3], "assigned_to": row[4], "created_at": row[5], "updated_at": row[6], "is_my_task": False} for row in cursor.fetchall()]

        # ==========================================
        # 👔 MANAGER LOGIC
        # ==========================================
        elif current_user['role'] == 'manager':
            cursor.execute("SELECT uuid, username FROM users WHERE role = 'employee' AND created_by = %s", (current_user['id'],))
            users = [{"uuid": row[0], "username": row[1], "role": 'employee'} for row in cursor.fetchall()]

            cursor.execute("SELECT COUNT(*) FROM users WHERE role = 'employee' AND created_by = %s", (current_user['id'],))
            admin_stats['total_employees'] = cursor.fetchone()[0]

            cursor.execute("SELECT username FROM users WHERE role = 'employee' AND created_by = %s", (current_user['id'],))
            admin_stats['my_created_users'] = [{"username": row[0], "role": "employee", "creator": "You"} for row in cursor.fetchall()]

            cursor.execute("""
                SELECT t.uuid, t.title, t.description, t.status, IFNULL(u_to.username, 'Unassigned') as assigned_to, IFNULL(u_by.username, 'System') as assigned_by, t.assigned_to as assigned_to_id,
                       DATE_FORMAT(t.created_at, '%d-%b-%Y %h:%i %p'), DATE_FORMAT(t.updated_at, '%d-%b-%Y %h:%i %p')
                FROM tasks t LEFT JOIN users u_to ON t.assigned_to = u_to.id LEFT JOIN users u_by ON t.assigned_by = u_by.id
                WHERE (t.assigned_by = %s OR t.assigned_to = %s) AND t.is_active = 1
            """, (current_user['id'], current_user['id']))
            for row in cursor.fetchall():
                tasks.append({"uuid": row[0], "title": row[1], "description": row[2], "status": row[3], "assigned_to": row[4], "assigned_by": row[5], "created_at": row[7], "updated_at": row[8], "is_my_task": True if row[6] == current_user['id'] else False})

        # ==========================================
        # 👷 EMPLOYEE LOGIC
        # ==========================================
        elif current_user['role'] == 'employee':
            cursor.execute("""
                SELECT t.uuid, t.title, t.description, t.status, IFNULL(u.username, 'System') as assigned_by,
                       DATE_FORMAT(t.created_at, '%d-%b-%Y %h:%i %p'), DATE_FORMAT(t.updated_at, '%d-%b-%Y %h:%i %p')
                FROM tasks t LEFT JOIN users u ON t.assigned_by = u.id WHERE t.assigned_to = %s AND t.is_active = 1
            """, (current_user['id'],))
            tasks = [{"uuid": row[0], "title": row[1], "description": row[2], "status": row[3], "assigned_by": row[4], "created_at": row[5], "updated_at": row[6], "is_my_task": True} for row in cursor.fetchall()]

        return jsonify({"users": users, "tasks": tasks, "admin_stats": admin_stats, "chart_data": chart_data}), 200

    except Exception as e: return jsonify({"message": f"Error: {str(e)}"}), 500
    finally:
        if cursor: cursor.close()
        if conn: conn.close()