from flask import Flask, jsonify, render_template, request
import os
from dotenv import load_dotenv

from extensions import mail

from routs.token_required import token_required
from routs.login import login_routs
from routs.admin_create_users import admin_create_user_route
from routs.admin_create_tasks import admin_create_task_route
from routs.delete import delete_routs
from routs.update import update_routs

from routs.manager_create_emp import manager_create_emp_route
from routs.manager_create_tasks import manager_create_task_route
from routs.dashboard_data import get_dashboard_data_route # 👈 YE ZARURI HAI

load_dotenv()

app = Flask(__name__)
app.json.sort_keys = False
app.config['SECRET_KEY'] = os.getenv('key')

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.getenv('sender_email')
app.config['MAIL_PASSWORD'] = os.getenv('sender_password')

mail.init_app(app)

# ====================
# FRONTEND ROUTES 
# ====================
@app.route('/', methods=['GET'])
def home():
    return render_template('login.html')

@app.route('/dashboard', methods=['GET'])
def dashboard_page():
    return render_template('dashboard.html')


# ====================
# BACKEND API ROUTES
# ====================
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    return login_routs()

@app.route('/dashboard-data', methods=['GET'])
@token_required
def dashboard_data(current_user):
    return get_dashboard_data_route(current_user)

@app.route('/admin/create-users', methods=['POST'])
@token_required  
def create_user(current_user): 
    return admin_create_user_route(current_user)

@app.route('/admin/create-tasks', methods = ['POST'])
@token_required
def create_tasks_from_admin(current_user):
    return admin_create_task_route(current_user)

@app.route('/manager/create-emp', methods = ['POST'])
@token_required
def create_emp(current_user):
    return manager_create_emp_route(current_user)

@app.route('/manager/create-tasks', methods = ['POST'])
@token_required
def create_tasks_from_manager(current_user):
    return manager_create_task_route(current_user)

@app.route('/delete/<string:uuid>', methods= ['DELETE'])
@token_required
def delete(current_user,uuid):
    return delete_routs(current_user, uuid)

@app.route('/update/<string:uuid>', methods = ['PUT'])
@token_required
def update(current_user,uuid):
    return update_routs(current_user,uuid)

if __name__ == "__main__":
    app.run(debug=True)