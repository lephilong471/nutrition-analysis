
import os
from datetime import timedelta

class Config:
    # Cấu hình kết nối đến MySQL
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@127.0.0.1/business_intelligence'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = 'Business Intelligence'
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=1)