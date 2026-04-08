from flask import Flask, request, jsonify
from models import db, User
from flask_bcrypt import Bcrypt
from flask_jwt_extended import (
    JWTManager,
    create_access_token,
    create_refresh_token,
    set_access_cookies,
    set_refresh_cookies,
    unset_jwt_cookies,
    jwt_required,
    get_jwt_identity
)
from datetime import timedelta

app = Flask(__name__)

# =========================
# ⚙️ CONFIG
# =========================
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"
app.config["JWT_SECRET_KEY"] = "super-secret-key"

app.config["JWT_TOKEN_LOCATION"] = ["cookies"]
app.config["JWT_COOKIE_SECURE"] = False   # True in production
app.config["JWT_COOKIE_SAMESITE"] = "Lax"
app.config["JWT_COOKIE_CSRF_PROTECT"] = True

app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(minutes=15)
app.config["JWT_REFRESH_TOKEN_EXPIRES"] = timedelta(days=7)

db.init_app(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

# =========================
# 🏁 INIT DB
# =========================
with app.app_context():
    db.create_all()

# =========================
# 📝 SIGNUP
# =========================
@app.route("/signup", methods=["POST"])
def signup():
    data = request.get_json()

    username = data.get("username")
    password = data.get("password")

    if User.query.filter_by(username=username).first():
        return jsonify({"msg": "User exists"}), 400

    hashed_pw = bcrypt.generate_password_hash(password).decode("utf-8")

    user = User(username=username, password=hashed_pw)
    db.session.add(user)
    db.session.commit()

    return jsonify({"msg": "User created"})

# =========================
# 🔐 LOGIN
# =========================
@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()

    user = User.query.filter_by(username=data.get("username")).first()

    if not user or not bcrypt.check_password_hash(user.password, data.get("password")):
        return jsonify({"msg": "Bad credentials"}), 401

    access_token = create_access_token(identity=str(user.id))
    refresh_token = create_refresh_token(identity=str(user.id))

    response = jsonify({"msg": "login success"})

    set_access_cookies(response, access_token)
    set_refresh_cookies(response, refresh_token)

    return response

# =========================
# 🔒 PROTECTED
# =========================
@app.route("/protected", methods=["POST"])
@jwt_required()
def protected():
    user_id = get_jwt_identity()
    return jsonify({"user_id": user_id})

# =========================
# 🔄 REFRESH
# =========================
@app.route("/refresh", methods=["POST"])
@jwt_required(refresh=True)
def refresh():
    user_id = get_jwt_identity()
    new_access = create_access_token(identity=str(user_id))

    response = jsonify({"msg": "refreshed"})
    set_access_cookies(response, new_access)

    return response

# =========================
# 🚪 LOGOUT
# =========================
@app.route("/logout", methods=["POST"])
def logout():
    response = jsonify({"msg": "logout"})
    unset_jwt_cookies(response)
    return response

# =========================
# ▶ RUN
# =========================
if __name__ == "__main__":
    app.run(debug=True)