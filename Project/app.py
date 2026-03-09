from flask import Flask , request , jsonify
from flask_mysqldb import MySQL
from werkzeug.security import generate_password_hash , check_password_hash
app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '1234' 
app.config['MYSQL_DB'] = 'my_db'

mysql = MySQL(app)


@app.route('/register' , methods = ['POST'])
def register():
    if request.method == 'POST':
            
        data = request.get_json()
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')
        
        if not username or not password:
            return jsonify({"message" : "Username and password are required"}), 400

        hash_password = generate_password_hash(password)

        conn = mysql.connection.cursor()
        try:
            conn.execute("INSERT INTO users (username, email, password) VALUES (%s, %s, %s)", (username, email, hash_password))
            mysql.connection.commit()

            return jsonify({"message" : "register successfully"}), 201
        
        except Exception as e:
             return jsonify({"error": "Email already exist"}), 409
        finally:
            conn.close()


@app.route('/login', methods = ['POST'])
def login():
    if request.method == "POST":
        data = request.get_json()
        email = data.get('email')
        password = data.get('password')

        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM users WHERE email = %s" , (email,))
        user = cursor.fetchone()
        cursor.close()

        if user and check_password_hash(user[3],password):
            return jsonify({"message" : f"login successful Welcome {user[1]}",
                            "user_id" : user[0]
            }), 200
        
        else:
            return jsonify({"error": "Invalid email and password"}), 401



if __name__ == "__main__":
    app.run(debug=True)