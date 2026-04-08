from flask import request, jsonify
from extensions import db, mail
from models import User
from werkzeug.security import generate_password_hash 
import os 
from flask_mail import Message

def manager_create_emp_route(current_user):
    if current_user['role'] != 'manager':
        return jsonify({"message": "You are not a Manager. Access Denied."}), 403
            
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    if not all([username, email, password]):
        return jsonify({"message": "Missing required fields"}), 400

    try:
        if User.query.filter_by(email=email).first():
            return jsonify({"message": "Email already exists"}), 409

        hashed_password = generate_password_hash(password)
        new_emp = User(role='employee', username=username, email=email, password=hashed_password, created_by=current_user['id'])
        
        db.session.add(new_emp)
        db.session.commit()

        try:
            msg = Message(subject="Your Employee Account", sender=os.getenv('sender_email'), recipients=[email])
            msg.body = f"Welcome {username}!\nEmail: {email}\nPassword: {password}"
            mail.send(msg)
        except Exception:
            pass

        return jsonify({"message": "Employee created successfully"}), 201

    except Exception as e:
        db.session.rollback()
        return jsonify({"message": f"An error occurred: {str(e)}"}), 500