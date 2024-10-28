from flask import Flask, make_response, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Import models from the models package
from models import db
from models.hero import Hero
from models.heropower import HeroPower
from models.power import Power

app = Flask(__name__)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///superheroes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

db.init_app(app)
migrate = Migrate(app, db)

@app.route('/')
def index():
    return '<h1>Superhero Code Challenge</h1>'

@app.route("/heroes")
def heroes():
    heroes = Hero.query.all()
    response = [hero.to_dict(only=("id", "name", "super_name")) for hero in heroes]
    return jsonify(response)

@app.route('/heroes/<int:id>')
def heroes_by_id(id):
    hero = Hero.query.filter_by(id=id).first()
    if not hero:
        error_body = {"error": "Hero not found"}
        return make_response(jsonify(error_body), 404)
    return jsonify(hero.to_dict())

@app.route('/powers')
def powers():
    powers = [power.to_dict(only=('description', 'id', 'name')) for power in Power.query.all()]
    return jsonify(powers)

@app.route('/powers/<int:id>', methods=['GET', 'PATCH'])
def powers_by_id(id):
    power = Power.query.filter_by(id=id).first()
    if not power:
        error_body = {"error": "Power not found"}
        return make_response(jsonify(error_body), 404)

    if request.method == 'GET':
        return jsonify(power.to_dict(only=('description', 'id', 'name')))
    
    elif request.method == 'PATCH':
        validation_errors = []
        if 'description' in request.json:
            description_value = request.json.get('description')
            if not isinstance(description_value, str) or len(description_value) < 20:
                validation_errors.append("Description must be at least 20 characters long.")
            else:
                power.description = description_value

        if validation_errors:
            return make_response(jsonify({"errors": validation_errors}), 400)

        db.session.commit()
        return jsonify(power.to_dict())

@app.route('/hero_powers', methods=['GET', 'POST'])
def hero_powers():
    if request.method == 'GET':
        hero_powers = HeroPower.query.all()
        return jsonify([hp.to_dict() for hp in hero_powers])

    elif request.method == 'POST':
        strength = request.json.get('strength')
        power_id = request.json.get('power_id')
        hero_id = request.json.get('hero_id')

        valid_strengths = {'Strong', 'Weak', 'Average'}
        if strength not in valid_strengths:
            return make_response(jsonify({"errors": ["Invalid strength. Choose from 'Strong', 'Weak', or 'Average'."]}), 400)

        new_hero_power = HeroPower(strength=strength, power_id=power_id, hero_id=hero_id)
        db.session.add(new_hero_power)
        db.session.commit()

        return jsonify(new_hero_power.to_dict()), 201

if __name__ == '__main__':
    app.run(port=5555, debug=True)
