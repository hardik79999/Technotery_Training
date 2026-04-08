from flask import jsonify
from models import User, Task
from sqlalchemy import or_

def get_dashboard_data_route(current_user):
    try:
        users_data = []
        tasks_data = []
        admin_stats = {}

        role = current_user['role']
        user_id = current_user['id']

        def format_date(dt):
            if dt:
                return dt.strftime('%d-%b-%Y %I:%M %p')
            return "N/A"

        # ==========================================
        # 👑 ADMIN SECTION
        # ==========================================
        if role == 'admin':
            
            # 1. get all user not in admin
            all_users = User.query.filter(User.role != 'admin').all()
            for u in all_users:
                # get who createed
                creator = User.query.filter_by(id=u.created_by).first()
                creator_name = creator.username if creator else 'System'

                users_data.append({
                    "uuid": u.uuid, "username": u.username, 
                    "role": u.role, "creator": creator_name
                })

            # 2. Total employees count
            admin_stats['total_employees'] = User.query.filter_by(role='employee').count()

            # 3. show all active tasks
            all_tasks = Task.query.filter_by(is_active=1).all()
            for t in all_tasks:
                # Find out the name of the person who has been assigned the task.
                assignee = User.query.filter_by(id=t.assigned_to).first()
                assignee_name = assignee.username if assignee else 'Unassigned'

                tasks_data.append({
                    "uuid": t.uuid, "title": t.title, "description": t.description, 
                    "status": t.status, "assigned_to": assignee_name,
                    "created_at": format_date(t.created_at), 
                    "updated_at": format_date(t.updated_at), "is_my_task": False
                })

        # ==========================================
        # 👔 MANAGER SECTION
        # ==========================================
        elif role == 'manager':
            
            # 1. Fire the employees I hired.
            my_employees = User.query.filter_by(role='employee', created_by=user_id).all()
            for u in my_employees:
                users_data.append({"uuid": u.uuid, "username": u.username, "role": u.role})

            admin_stats['total_employees'] = len(my_employees)
            admin_stats['my_created_users'] = [
                {"username": u.username, "role": "employee", "creator": "You"} for u in my_employees
            ]

            # 2. Mere tasks nikalo (Jo maine diye hain YA mujhe mile hain)
            manager_tasks = Task.query.filter(or_(Task.assigned_by == user_id, Task.assigned_to == user_id), Task.is_active == 1).all()
            
            for t in manager_tasks:
                assignee = User.query.filter_by(id=t.assigned_to).first()
                assigner = User.query.filter_by(id=t.assigned_by).first()

                assignee_name = assignee.username if assignee else 'Unassigned'
                assigner_name = assigner.username if assigner else 'System'

                tasks_data.append({
                    "uuid": t.uuid, 
                    "title": t.title, 
                    "description": t.description, 
                    "status": t.status, 
                    "assigned_to": assignee_name, 
                    "assigned_by": assigner_name,
                    "created_at": format_date(t.created_at), 
                    "updated_at": format_date(t.updated_at), 
                    "is_my_task": (t.assigned_to == user_id)
                })

        # ==========================================
        # 👷 EMPLOYEE SECTION
        # ==========================================
        elif role == 'employee':
            
            # 1. Show me only my tasks.
            emp_tasks = Task.query.filter_by(assigned_to=user_id, is_active=1).all()
            
            for t in emp_tasks:
                assigner = User.query.filter_by(id=t.assigned_by).first()
                assigner_name = assigner.username if assigner else 'System'

                tasks_data.append({
                    "uuid": t.uuid, "title": t.title, "description": t.description, 
                    "status": t.status, "assigned_by": assigner_name,
                    "created_at": format_date(t.created_at), 
                    "updated_at": format_date(t.updated_at), "is_my_task": True
                })

        return jsonify({"users": users_data, "tasks": tasks_data, "admin_stats": admin_stats}), 200

    except Exception as e:
        return jsonify({"message": f"Error: {str(e)}"}), 500