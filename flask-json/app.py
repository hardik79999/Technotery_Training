from flask import Flask, request, jsonify
from flask_mysqldb import MySQL
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '1234' 
app.config['MYSQL_DB'] = 'auth_db'

mysql = MySQL(app)





@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    hashed_password = generate_password_hash(password)

    cur = mysql.connection.cursor()
    try:
        cur.execute("INSERT INTO users (username, email, password) VALUES (%s, %s, %s)", (username, email, hashed_password))
        mysql.connection.commit()
        print(email)
        return jsonify({"message": "register successfully!"}), 201
    except Exception as e:
    
        return jsonify({"error": "Email or already exist"}), 400
    finally:
        cur.close()


@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM users WHERE email = %s", (email,))
    user = cur.fetchone()
    cur.close()

    if user and check_password_hash(user[3], password):
        return jsonify({
            "message": f"Login successful! Welcome {user[1]}", 
            "user_id": user[0]
        }), 200
    else:
        return jsonify({"error": "Invalid email and password"}), 401

if __name__ == '__main__':
    app.run(debug=True)