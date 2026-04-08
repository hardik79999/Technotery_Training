from flask import request, jsonify
from werkzeug.security import check_password_hash
import datetime
import jwt
import os
from database import database

def login_routs():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    conn = None
    cursor = None

    if not email or not password :
        return jsonify({"message":"email, password are required"}), 400

    try:
        conn = database()
        conn.autocommit = False
        cursor = conn.cursor()

        query = """
                SELECT id, uuid, role, username, email , password
                FROM users
                WHERE email=%s
            """
        values = (email,)
        cursor.execute(query, values)
        user = cursor.fetchone()

        if user and check_password_hash(user[5],password):
            payload = {
                "id": user[0],
                "uuid": user[1],
                "role": user[2],
                "username": user[3],
                "exp": datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(days=7)
            }

            token = jwt.encode(payload, os.getenv('key'), algorithm="HS256")
            
            return jsonify({
                'message': 'Login successful',
                'role': user[2],
                'username': user[3], # 🚀 YE LINE MISSING THI
                'token': token
            }), 200
            
        else:
            return jsonify({"message": "Invalid email or password"}), 401
        
    except Exception as e:
        if conn:
            conn.rollback()
        return jsonify({"message": f"An error occurred: {str(e)}"}), 500
    
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()