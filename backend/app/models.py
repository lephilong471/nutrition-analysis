from . import db

class Users(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(250), nullable=False)
    role = db.Column(db.Integer, nullable=False)
    status = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'

class NutritionData(db.Model):
    __tablename__ = 'nutrition_data'  # Tên bảng trong cơ sở dữ liệu

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # Khóa chính tự động tăng
    food = db.Column(db.String(255), nullable=False)  # Tên hoặc loại thực phẩm
    link = db.Column(db.String(255), nullable=False)
    group = db.Column(db.String(255), nullable=False)
    caloric_value = db.Column(db.Float, nullable=False)  # Tổng năng lượng (kcal/100g)
    fat = db.Column(db.Float, nullable=False)  # Tổng lượng chất béo (g/100g)
    saturated_fats = db.Column(db.Float, nullable=False)  # Lượng chất béo bão hòa (g/100g)
    monounsaturated_fats = db.Column(db.Float, nullable=False)  # Lượng chất béo không bão hòa đơn (g/100g)
    polyunsaturated_fats = db.Column(db.Float, nullable=False)  # Lượng chất béo không bão hòa đa (g/100g)
    carbohydrates = db.Column(db.Float, nullable=False)  # Tổng carbohydrates (g/100g)
    sugars = db.Column(db.Float, nullable=False)  # Tổng lượng đường (g/100g)
    protein = db.Column(db.Float, nullable=False)  # Tổng lượng protein (g/100g)
    dietary_fiber = db.Column(db.Float, nullable=False)  # Lượng chất xơ (g/100g)
    cholesterol = db.Column(db.Float, nullable=False)  # Lượng cholesterol (mg/100g)
    sodium = db.Column(db.Float, nullable=False)  # Lượng natri (mg/100g)
    water = db.Column(db.Float, nullable=False)  # Lượng nước (g/100g)
    vitamin_a = db.Column(db.Float, nullable=False)  # Lượng vitamin A (µg/100g)
    vitamin_b1 = db.Column(db.Float, nullable=False)  # Lượng vitamin B1 (Thiamine) (mg/100g)
    vitamin_b11 = db.Column(db.Float, nullable=False)  # Lượng vitamin B11 (Folic Acid) (mg/100g)
    vitamin_b12 = db.Column(db.Float, nullable=False)  # Lượng vitamin B12 (mg/100g)
    vitamin_b2 = db.Column(db.Float, nullable=False)  # Lượng vitamin B2 (Riboflavin) (mg/100g)
    vitamin_b3 = db.Column(db.Float, nullable=False)  # Lượng vitamin B3 (Niacin) (mg/100g)
    vitamin_b5 = db.Column(db.Float, nullable=False)  # Lượng vitamin B5 (Pantothenic Acid) (mg/100g)
    vitamin_b6 = db.Column(db.Float, nullable=False)  # Lượng vitamin B6 (mg/100g)
    vitamin_c = db.Column(db.Float, nullable=False)  # Lượng vitamin C (mg/100g)
    vitamin_d = db.Column(db.Float, nullable=False)  # Lượng vitamin D (mg/100g)
    vitamin_e = db.Column(db.Float, nullable=False)  # Lượng vitamin E (mg/100g)
    vitamin_k = db.Column(db.Float, nullable=False)  # Lượng vitamin K (mg/100g)
    calcium = db.Column(db.Float, nullable=False)  # Lượng calcium (mg/100g)
    copper = db.Column(db.Float, nullable=False)  # Lượng copper (mg/100g)
    iron = db.Column(db.Float, nullable=False)  # Lượng iron (mg/100g)
    magnesium = db.Column(db.Float, nullable=False)  # Lượng magnesium (mg/100g)
    manganese = db.Column(db.Float, nullable=False)  # Lượng manganese (mg/100g)
    phosphorus = db.Column(db.Float, nullable=False)  # Lượng phosphorus (mg/100g)
    potassium = db.Column(db.Float, nullable=False)  # Lượng potassium (mg/100g)
    selenium = db.Column(db.Float, nullable=False)  # Lượng selenium (mg/100g)
    zinc = db.Column(db.Float, nullable=False)  # Lượng zinc (mg/100g)
    nutrition_density = db.Column(db.Float, nullable=False)  # Độ giàu dinh dưỡng của thực phẩm

    def __repr__(self):
        return f'Name: {self.food}, Selenium: {self.selenium}'