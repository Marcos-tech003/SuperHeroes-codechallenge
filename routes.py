from flask import Blueprint, jsonify, request
from models import db, Hero, Power, HeroPower

routes = Blueprint('routes', __name__)

# GET /heroes
@routes.route('/heroes', methods=['GET'])
def get_heroes():
    heroes = Hero.query.all()
    return jsonify([hero.to_dict() for hero in heroes]), 200

# GET /heroes/:id
@routes.route('/heroes/<int:id>', methods=['GET'])
def get_hero(id):
    hero = Hero.query.get(id)
    if not hero:
        return jsonify({'error': 'Hero not found'}), 404
    return jsonify(hero.to_dict()), 200

# GET /powers
@routes.route('/powers', methods=['GET'])
def get_powers():
    powers = Power.query.all()
    return jsonify([power.to_dict() for power in powers]), 200

# GET /powers/:id
@routes.route('/powers/<int:id>', methods=['GET'])
def get_power(id):
    power = Power.query.get(id)
    if not power:
        return jsonify({'error': 'Power not found'}), 404
    return jsonify(power.to_dict()), 200

# PATCH /powers/:id
@routes.route('/powers/<int:id>', methods=['PATCH'])
def update_power(id):
    power = Power.query.get(id)
    if not power:
        return jsonify({'error': 'Power not found'}), 404
    
    try:
        data = request.get_json()
        power.validate_description(data['description'])
        power.description = data['description']
        db.session.commit()
        return jsonify(power.to_dict()), 200
    except ValueError as e:
        return jsonify({'errors': [str(e)]}), 400
