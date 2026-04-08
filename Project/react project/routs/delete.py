from flask import request, jsonify
from database import database

def delete_routs(current_user, uuid):
    conn = None
    cursor = None

    try:
        conn = database()
        conn.autocommit = False
        cursor = conn.cursor()
        
        if current_user['role'] == "admin":
            query = """
                UPDATE tasks
                SET is_active = 0
                WHERE uuid = %s
            """
            values = (uuid,)
            
        elif current_user['role'] == "manager":
            query = """
                UPDATE tasks
                SET is_active = 0
                WHERE uuid = %s AND assigned_by = %s
            """
            values = (uuid, current_user['id'])
            
        else:
            return jsonify({"message": "Employees are not allowed to delete tasks."}), 403

        cursor.execute(query, values) 
        conn.commit()

        if cursor.rowcount <= 0:
            return jsonify({
                "message": "Task not found or you are not authorized"
            }), 403
        
        return jsonify({
            "username": current_user['username'],
            "message": "Task deleted successfully!"
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