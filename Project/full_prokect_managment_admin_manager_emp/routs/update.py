from flask import request, jsonify
from extensions import db
from models import Task

def update_routs(current_user, uuid):
    data = request.get_json()
    new_status = data.get('status')
    new_title = data.get('title')
    new_description = data.get('description')
    
    if not any([new_status, new_title, new_description]):
        return jsonify({"message": "Provide at least one field to update"}), 400

    try:
        task = Task.query.filter_by(uuid=uuid, is_active=1).first()
        if not task:
            return jsonify({"message": "Task not found!"}), 404

        role = current_user['role']
        user_id = current_user['id']

        if role == "employee":
            if task.assigned_to != user_id:
                return jsonify({"message": "Access Denied!"}), 403
            if new_title or new_description:
                 return jsonify({"message": "Employees can only update 'status'."}), 403
            if new_status in ['pending', 'in progress', 'completed']:
                task.status = new_status
            else:
                return jsonify({"message": "Invalid status."}), 400

        elif role == "manager":
            if task.assigned_to == user_id:
                if new_title or new_description:
                    return jsonify({"message": "You can only update 'status' for tasks assigned to you."}), 403
                if new_status in ['pending', 'in progress', 'completed']:
                    task.status = new_status
            
            elif task.assigned_by == user_id:
                if new_title: task.title = new_title
                if new_description: task.description = new_description
                if new_status: task.status = new_status
            else:
                return jsonify({"message": "Access Denied! This is not your task."}), 403

        elif role == 'admin':
            if new_title: task.title = new_title
            if new_description: task.description = new_description
            if new_status: task.status = new_status

        db.session.commit()
        return jsonify({"username": current_user['username'], "message": "Task updated successfully!"}), 200
        
    except Exception as e:
        db.session.rollback()
        return jsonify({"message": f"An error occurred: {str(e)}"}), 500