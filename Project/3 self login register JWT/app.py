from flask import Flask, request
from dotenv import load_dotenv
import os

from routes.token_required import token_required
from routes.register import register_routes
from routes.login import login_routes
from routes.profile import profile_routes
from routes.post import post_routes
from routes.all_post import all_post_routes
from routes.public_post import public_post_routes
from routes.update import update_routes
from routes.delete_post import delete_post_routes
from routes.find_post import find_post_routes
from routes.search_post import search_post_routs

load_dotenv()

app = Flask(__name__)
app.json.sort_keys = False
app.config['SECRET_KEY'] = os.getenv('key')



@app.route('/register', methods=['POST'])
def register():
    return register_routes()



@app.route('/login', methods=['POST'])
def login():
    return login_routes()



@app.route('/profile', methods=['GET'])
@token_required
def profile(current_user_name):
    return profile_routes(current_user_name)



@app.route('/post', methods=['POST'])
@token_required
def post(current_user_name):
    return post_routes(current_user_name)



@app.route('/all_post', methods=['GET'])
@token_required
def all_post(current_user_name):
    return all_post_routes(current_user_name)



@app.route('/public_post', methods=['GET'])
def public_post():
    page = int(request.args.get("page",1))
    limit = int(request.args.get("limit",10))
    return public_post_routes(page, limit)


@app.route('/update_post/<uuid>', methods=['PUT'])
@token_required
def update(current_user_name, uuid):
    return update_routes(current_user_name, uuid)



@app.route('/delete_post/<uuid>', methods=['DELETE'])
@token_required
def delete_post(current_user_name, uuid):
    return delete_post_routes(current_user_name, uuid)



@app.route('/find_post/<uuid>', methods=['GET'])
def find_post(uuid):
    return find_post_routes(uuid)


@app.route('/search_post', methods = ['GET'])
def serch_post():
    page = int(request.args.get("page",1))
    limit = int(request.args.get("limit",10))
    find = request.args.get("find")
    return search_post_routs(page, limit, find)


if __name__ == "__main__":
    app.run(debug=True)