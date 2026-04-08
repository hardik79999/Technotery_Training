from flask import request, jsonify
from database import database
from werkzeug.security import generate_password_hash 
import os 

from extensions import mail
from flask_mail import Message

def admin_create_user_route(current_user):
    if current_user['role'] != 'admin':
        return jsonify({"message": "You are not an Admin. Access Denied."}), 403
    
            
    data = request.get_json()
    role = data.get('role')
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')


    if not role or not username or not email or not password:
        return jsonify({"message": "Missing required fields"}), 400

    if role not in ['manager', 'employee']:
        return jsonify({"message": "Role must be manager or employee"}), 400


    conn = None
    cursor = None


    try:
        conn = database()
        conn.autocommit = False
        cursor = conn.cursor()


        cursor.execute("SELECT uuid FROM users WHERE email = %s", (email,))
        
        if cursor.fetchone():
            return jsonify({"message": "Email already exists"}), 409

        hashed_password = generate_password_hash(password)

        users_query = """
                INSERT INTO users (role, username, email, password)
                VALUES (%s, %s, %s, %s) 
        """
        users_values = (role, username, email, hashed_password)
        cursor.execute(users_query, users_values)
        
        
        conn.commit()

        try:
            msg = Message(
                subject=f"Welcome to Task Management System - Your {role} Account",
                sender=os.getenv('sender_email'),
                recipients=[email]
            )
            
            # Professional English Format (Left-aligned to avoid weird spacing in email)
            msg.body = f"""Dear {username},

Welcome to the Task Management System!

Your account has been successfully created with the role of '{role}'. Below are your official login credentials:

Email: {email}
Password: {password}

Please log in to the system to access your dashboard and start your work. We highly recommend keeping your credentials secure.

Best Regards,
The Admin Team"""
            
            mail.send(msg)
            print("Email sent successfully to", email)
        except Exception as e:
            print("Failed to send email:", str(e))
            

        return jsonify({"message": f"{role} created successfully"}), 201



    except Exception as e:
        if conn:
            conn.rollback()
        return jsonify({"message": f"An error occurred: {str(e)}"}), 500
    


    finally:
        if cursor: cursor.close()
        if conn: conn.close()