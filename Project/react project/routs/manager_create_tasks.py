from flask import request , jsonify
from database import database


def manager_create_task_route(current_user):
    if current_user['role'] != 'manager':
        return jsonify({"message": "You are not an manager. Access Denied."}), 403
            
    data = request.get_json()
    title = data.get('title')
    description = data.get('description')
    assigned_to = data.get('assigned_to') 

    if not title or not assigned_to:
        return jsonify({"message": "Title and assigned_to are required"}), 400

    conn = None
    cursor = None

    try:
        conn = database()
        conn.autocommit = False
        cursor = conn.cursor()

        cursor.execute("SELECT id FROM users WHERE uuid = %s", (assigned_to,))
        current_assigned = cursor.fetchone()

        if not current_assigned:
            return jsonify({"message": "Invalid UUID! Employee not found."}), 404

        tasks_query = """
                INSERT INTO tasks (title, description, assigned_to, assigned_by)
                VALUES (%s, %s, %s, %s)
        """
        tasks_values = (title, description, current_assigned[0], current_user['id'])
        
        cursor.execute(tasks_query, tasks_values)
        conn.commit()

        return jsonify({"message": "Task assigned successfully"}), 201

    except Exception as e:
        if conn:
            conn.rollback()
        return jsonify({"message": f"An error occurred: {str(e)}"}), 500
    
    
    finally:
        if cursor: cursor.close()
        if conn: conn.close()