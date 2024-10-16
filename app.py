from flask import Flask, make_response, request
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
app.json.compact = False

db.init_app(app)
migrate = Migrate(app, db)

@app.route('/')
def index():
    return '<h1>Superhero Code Challenge</h1>'

@app.route("/heroes")
def heroes():
    heroes = Hero.query.all()
    response = [hero.to_dict(only=("id", "name", "super_name")) for hero in heroes]
    return make_response(response, 200)

@app.route('/heroes/<int:id>')
def heroes_by_id(id):
    hero = Hero.query.filter(Hero.id == id).first()
    if not hero:
        error_body = {"error": "Hero not found"}
        return make_response(error_body, 404)

    return make_response(hero.to_dict(), 200)

@app.route('/powers')
def powers():
    powers = [power.to_dict(only=('description', 'id', 'name')) for power in Power.query.all()]
    return make_response(powers, 200)

@app.route('/powers/<int:id>', methods=['GET', 'PATCH'])
def powers_by_id(id):
    power = Power.query.filter(Power.id == id).first()
    if not power:
        error_body = {"error": "Power not found"}
        return make_response(error_body, 404)

    if request.method == 'GET':
        return make_response(power.to_dict(only=('description', 'id', 'name')), 200)

    elif request.method == 'PATCH':
        validation_errors = []

        for attr in request.json:
            if attr == 'description':
                description_value = request.json.get(attr)
                if not isinstance(description_value, str) or len(description_value) < 20:
                    validation_errors.append("Description must be at least 20 characters long.")
            else:
                setattr(power, attr, request.json.get(attr))

        if validation_errors:
            return make_response({"errors": validation_errors}, 400)

        for attr in request.json:
            setattr(power, attr, request.json.get(attr))

        db.session.commit()
        return make_response(power.to_dict(), 200)

@app.route('/hero_powers', methods=['GET', 'POST'])
def hero_powers():
    if request.method == 'GET':
        hero_power = HeroPower.query.all()
        return make_response([hero_power.to_dict() for hero_power in hero_power], 200)

    elif request.method == 'POST':
        strength = request.json.get('strength')
        power_id = request.json.get('power_id')
        hero_id = request.json.get('hero_id')

        valid_strengths = {'Strong', 'Weak', 'Average'}
        if strength not in valid_strengths:
            return make_response({"errors": ["validation errors"]}, 400)

        new_power = HeroPower(strength=strength, power_id=power_id, hero_id=hero_id)
        db.session.add(new_power)
        db.session.commit()

        return make_response(new_power.to_dict(), 200)

if __name__ == '__main__':
    app.run(port=5555, debug=True)
