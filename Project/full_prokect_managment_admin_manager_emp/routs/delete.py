from flask import request, jsonify
from extensions import db
from models import Task

def delete_routs(current_user, uuid):
    try:
        task = Task.query.filter_by(uuid=uuid, is_active=1).first()
        if not task:
            return jsonify({"message": "Task not found"}), 404

        if current_user['role'] == "admin":
            task.is_active = 0
        elif current_user['role'] == "manager":
            if task.assigned_by != current_user['id']:
                return jsonify({"message": "Not authorized"}), 403
            task.is_active = 0
        else:
            return jsonify({"message": "Employees are not allowed to delete tasks."}), 403

        db.session.commit()
        return jsonify({"username": current_user['username'], "message": "Task deleted successfully!"}), 200

    except Exception as e:
        db.session.rollback()
        return jsonify({"message": f"An error occurred: {str(e)}"}), 500