from flask import request, jsonify
from extensions import db, mail
from models import User
from werkzeug.security import generate_password_hash 
import os 
from flask_mail import Message
import jwt
import datetime

def admin_create_user_route(current_user):
    if current_user['role'] != 'admin':
        return jsonify({"message": "You are not an Admin. Access Denied."}), 403
            
    data = request.get_json()
    role = data.get('role')
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    if not all([role, username, email, password]):
        return jsonify({"message": "Missing required fields"}), 400

    try:
        if User.query.filter_by(email=email).first():
            return jsonify({"message": "Email already exists"}), 409

        hashed_password = generate_password_hash(password)
        
        # add new user
        new_user = User(role=role, username=username, email=email, password=hashed_password, created_by=current_user['id'])
        db.session.add(new_user)
        db.session.commit()

        # Token & Email Logic
        token_payload = {"email": email, "role": role, "exp": datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(hours=24)}
        email_token = jwt.encode(token_payload, os.getenv('key'), algorithm="HS256")
        magic_link = f"http://127.0.0.1:5000/login?token={email_token}"

        try:
            msg = Message(subject=f"Your {role.capitalize()} Account", sender=os.getenv('sender_email'), recipients=[email])
            msg.body = f"Welcome {username}!\nEmail: {email}\nPassword: {password}\nLogin here: {magic_link}"
            mail.send(msg)
        except Exception:
            pass

        return jsonify({"message": f"{role.capitalize()} created successfully"}), 201

    except Exception as e:
        db.session.rollback()
        return jsonify({"message": f"An error occurred: {str(e)}"}), 500