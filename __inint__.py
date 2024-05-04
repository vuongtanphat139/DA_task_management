from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Khởi tạo ứng dụng Flask
application = Flask(__name__)

# Cấu hình cơ sở dữ liệu
application.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Khởi tạo đối tượng SQLAlchemy
db = SQLAlchemy(application)