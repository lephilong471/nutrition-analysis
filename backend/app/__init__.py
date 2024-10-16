from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_cors import CORS
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    CORS(app)
    jwt = JWTManager(app)

    # Cấu hình kết nối đến MySQL
    app.config.from_object('config.Config')

    # Khởi tạo database
    db.init_app(app)

    # Đăng ký routes
    from app.routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app