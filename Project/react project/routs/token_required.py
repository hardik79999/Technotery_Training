from flask import request, jsonify
from functools import wraps
import jwt
import os
from database import database # Naya import

def token_required(f):
    @wraps(f)
    def token(*args , **kwargs):
        auth_header = request.headers.get('Authorization')

        if not auth_header or not auth_header.startswith("Bearer "):
            return jsonify({"message": 'Token is missing or invalid format!'}), 401

        conn = None
        cursor = None
        try:
            token_string = auth_header.split(" ")[1]
            decoded_payload = jwt.decode(token_string, os.getenv('key'), algorithms=["HS256"])
            
            # 🚀 LIVE DB CHECK: Agar user DB se delete ho gaya, toh block karo!
            conn = database()
            cursor = conn.cursor()
            cursor.execute("SELECT id FROM users WHERE id = %s", (decoded_payload.get('id'),))
            if not cursor.fetchone():
                return jsonify({"message": "Account deleted! Access Denied."}), 401
            
            current_user = {
                "id": decoded_payload.get('id'),
                "uuid": decoded_payload.get('uuid'),
                "role": decoded_payload.get('role'),
                "username": decoded_payload.get('username')
            }

        except Exception as e:
            return jsonify({"message":"Token is invalid or expired!"}), 401
        finally:
            if cursor: cursor.close()
            if conn: conn.close()

        return f(current_user, *args, **kwargs)
    return token