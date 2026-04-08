import os
from dotenv import load_dotenv
from database import database  
from werkzeug.security import generate_password_hash
import mysql.connector

load_dotenv()

def database():
    return mysql.connector.connect(
        host = os.getenv('host'),
        user = os.getenv('user'),
        password = os.getenv('password'),
        database = os.getenv('database')
    )

def setup_admin():
    conn = None
    cursor = None
    try:
        conn = database()
        cursor = conn.cursor()

        admin_email = "admin@test.com"
        admin_password = "123"
        admin_username = "superadmin"
        admin_role = "admin"

        hashed_password = generate_password_hash(admin_password)

        cursor.execute("SELECT * FROM users WHERE email = %s", (admin_email,))
        if cursor.fetchone():
            print("admin already exist")
            return

        # Insert Query
        query = """
            INSERT INTO users (role, username, email, password)
            VALUES (%s, %s, %s, %s)
        """
        values = (admin_role, admin_username, admin_email, hashed_password)

        cursor.execute(query, values)
        conn.commit() 

      
    except Exception as e:
        print(f": {str(e)}")
    
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

if __name__ == "__main__":
    setup_admin()