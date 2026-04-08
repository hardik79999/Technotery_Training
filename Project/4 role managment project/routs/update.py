from flask import request, jsonify
from database import database

def update_routs(current_user, uuid):
    data = request.get_json()
    new_status = data.get('status')
    new_title = data.get('title')
    new_description = data.get('description')
    
    conn = None
    cursor = None

    if not new_status and not new_title and not new_description:
        return jsonify({"message": "Please provide at least one field to update"}), 400

    try:
        conn = database()
        conn.autocommit = False
        cursor = conn.cursor()

        cursor.execute("""SELECT assigned_to, assigned_by 
                       FROM tasks 
                       WHERE uuid = %s 
                       AND is_active = 1
                       """, (uuid,))
        task = cursor.fetchone()

        if not task:
            return jsonify({"message": "The task was not found or has been deleted!"}), 404

        task_assigned_to = task[0]
        task_assigned_by = task[1]

        if current_user['role'] == "employee":
            
            if task_assigned_to != current_user['id']: 
                return jsonify({"message": "Access Denied! You can only update your assigned tasks."}), 403
            
            if not new_status:
                return jsonify({"message": "Employees can only update their 'status'!"}), 400
            
            if new_title or new_description:
                 return jsonify({"message": "Not Allowed! Employees can only update 'status'."}), 403
            
            valid_statuses = ['pending', 'in progress', 'completed']
            if new_status not in valid_statuses:
                return jsonify({"message": f"Invalid status. Choose from: {valid_statuses}"}), 400

            query = """
                        UPDATE tasks SET status=%s
                        WHERE uuid = %s
                    """
            values = (new_status, uuid)
            
            cursor.execute(query, values)


        elif current_user['role'] == "manager":
            if task_assigned_by != current_user['id']:
                return jsonify({"message": "Access Denied! You can only update your assigned tasks."}), 403

            updates = []
            values = []
            if new_title:
                updates.append("title = %s")
                values.append(new_title)

            if new_description: 
                updates.append("description = %s")
                values.append(new_description)

            if new_status: 
                updates.append("status = %s")
                values.append(new_status)

            values.append(uuid)

            query = f"UPDATE tasks SET {', '.join(updates)} WHERE uuid = %s"
            cursor.execute(query, tuple(values))

        elif current_user['role'] == 'admin':
            
            updates = []
            values = []

            if new_title: 
                updates.append("title = %s")
                values.append(new_title)
            
            if new_description: 
                updates.append("description = %s")
                values.append(new_description)
            
            if new_status: 
                updates.append("status = %s")
                values.append(new_status)

            values.append(uuid)
            
            query = f"UPDATE tasks SET {', '.join(updates)} WHERE uuid = %s"
            cursor.execute(query, tuple(values))

        conn.commit()

        return jsonify({
            "username": current_user['username'],
            "message": "Task updated successfully!"
        }), 200
        
    except Exception as e:
        if conn:
            conn.rollback()
        return jsonify({"message": f"An error occurred: {str(e)}"}), 500

    finally:
        if cursor:
            cursor.close() 
        if conn:
            conn.close()