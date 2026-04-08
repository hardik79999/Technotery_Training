from flask import request, jsonify
from extensions import db
from models import User, Task

def admin_create_task_route(current_user):
    
    if current_user['role'] != 'admin':
        return jsonify({"message": "You are not an Admin. Access Denied."}), 403
            
    data = request.get_json()
    title = data.get('title')
    description = data.get('description')
    assigned_to_uuid = data.get('assigned_to')  # Frontend UUID

    if not title or not assigned_to_uuid:
        return jsonify({"message": "Title and assignee are required"}), 400

    try:
        assigned_user = User.query.filter_by(uuid=assigned_to_uuid).first()

        if not assigned_user:
            return jsonify({"message": "User not found!"}), 404

        new_task = Task(
            title=title, 
            description=description, 
            assigned_to=assigned_user.id, 
            assigned_by=current_user['id']
        )
        
        db.session.add(new_task)
        db.session.commit()

        return jsonify({"message": "Task assigned successfully"}), 201

    except Exception as e:
        db.session.rollback()
        return jsonify({"message": f"An error occurred: {str(e)}"}), 500