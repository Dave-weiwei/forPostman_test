from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import jwt, datetime
import os
from functools import wraps

app = Flask(__name__)
CORS(app)

# 應使用環境變數儲存
app.config['SECRET_KEY'] = 'bookstation-secret'

# 暫時用記憶體模擬資料庫
users = []
books = []
reviews = []

# 建立初始管理員帳號
users.append({"username": "admin@test.com", "password": "Admin123", "role": "admin"})

# JWT 驗證裝飾器
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            return jsonify({"error": "缺少授權 token"}), 401
        try:
            token = token.replace("Bearer ", "")
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
            current_user = next((u for u in users if u['username'] == data['username']), None)
            if not current_user:
                raise Exception("使用者不存在")
        except Exception as e:
            return jsonify({"error": "無效 token"}), 401
        return f(current_user, *args, **kwargs)
    return decorated

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")
    if not username or not password:
        return jsonify({"error": "帳號密碼不可為空"}), 400
    if any(u['username'] == username for u in users):
        return jsonify({"error": "帳號已存在"}), 409
    users.append({"username": username, "password": password, "role": "user"})
    return jsonify({"message": "註冊成功"}), 200

@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")
    user = next((u for u in users if u['username'] == username and u['password'] == password), None)
    if not user:
        return jsonify({"error": "帳號或密碼錯誤"}), 401

    token = jwt.encode({
        "username": user['username'],
        "role": user['role'],
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=2)
    }, app.config['SECRET_KEY'], algorithm="HS256")
    return jsonify({"token": token, "role": user['role']}), 200

@app.route("/profile", methods=["GET"])
@token_required
def profile(current_user):
    return jsonify({"username": current_user['username'], "role": current_user['role']}), 200

@app.route("/books", methods=["GET"])
def get_books():
    page = int(request.args.get("page", 1))
    limit = int(request.args.get("limit", 5))
    start = (page - 1) * limit
    end = start + limit
    paged_books = books[start:end]
    return jsonify({
        "data": paged_books,
        "pagination": {
            "page": page,
            "limit": limit,
            "total": len(books)
        }
    }), 200

@app.route("/books", methods=["POST"])
@token_required
def create_book(current_user):
    if current_user['role'] != 'admin':
        return jsonify({"error": "只有管理員可新增書籍"}), 403
    return jsonify({"message": "請實作上傳封面與書籍資訊的邏輯"}), 501  # 留給你自己實作

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # 本地預設 5000，Render 用它指定的
    app.run(debug=True, host="0.0.0.0", port=port)
