from flask import Blueprint, jsonify, request
from flask_jwt_extended import create_access_token, jwt_required, unset_jwt_cookies, get_jwt, get_jwt_identity
from datetime import datetime, timedelta, timezone
import bcrypt

from .models import Users

from .crud import crud_get_admin_credentials, crud_get_nutrition_data

main = Blueprint('main', __name__)

@main.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,true')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    return response

@main.after_request
def refresh_expiring_jwts(response):
    try:
        exp_timestamp = get_jwt()["exp"]
        now = datetime.now(timezone.utc)
        target_timestamp = datetime.timestamp(now + timedelta(minutes=30))
        if target_timestamp > exp_timestamp:
            access_token = create_access_token(identity=get_jwt_identity())
            data = response.get_json()
            if type(data) is dict:
                data["access_token"] = access_token 
                response.data = json.dumps(data)
        return response
    except (RuntimeError, KeyError):
        # Case where there is not a valid JWT. Just return the original respone
        return response

# Normal API
@main.route("/api/v1/get-nutrition-data", methods=['GET'])
def get_nutrition_data():
    result = crud_get_nutrition_data()
    data = [
        {
            'id': r.id, 
            'name': r.food.capitalize(), 
            'link': f'http://localhost:5000/static/images/{r.link}',
            'group': r.group
        } for r in result]

    return jsonify(data), 200

# Admin API
@main.route('/api/v1/admin/login', methods=['POST'])
def admin_login():
    username = request.json['username']
    password = request.json['password']
    b_password = password.encode()

    admin_credentials = crud_get_admin_credentials()

    if( username == admin_credentials.username and bcrypt.checkpw(b_password,admin_credentials.password.encode())):
        access_token = create_access_token(identity=admin_credentials.username)
        return jsonify({'token': access_token}), 200
    return jsonify({'error': 'Unauthorized!'}), 401

