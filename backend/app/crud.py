from .models import Users, NutritionData
from .database import SessionLocal


def crud_get_admin_credentials():
    db = SessionLocal()
    try:
        result = db.query(Users).filter(Users.role == 1, Users.status == 1).first() 
        return result
    finally:
        db.close()

def crud_get_nutrition_data():
    db = SessionLocal()
    try:
        result = db.query(NutritionData).all()
        return result
    finally:
        db.close()