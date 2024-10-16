from sqlalchemy.orm import validates
from sqlalchemy_serializer import SerializerMixin
from . import db  # Import db from the models __init__.py file

class HeroPower(db.Model, SerializerMixin):
    __tablename__ = 'hero_powers'

    id = db.Column(db.Integer, primary_key=True)
    strength = db.Column(db.String, nullable=False)
    hero_id = db.Column(db.Integer, db.ForeignKey('heroes.id'))
    power_id = db.Column(db.Integer, db.ForeignKey('powers.id'))

    # Relationships
    hero = db.relationship('Hero', back_populates='hero_powers')
    power = db.relationship('Power', back_populates='hero_powers')

    # Serialization rules
    serialize_rules = ('-hero.hero_powers', '-power.hero_powers')

    @validates('strength')
    def validate_strength(self, key, strength):
        valid_strengths = {'Strong', 'Weak', 'Average'}
        if strength not in valid_strengths:
            raise ValueError(f"Strength must be one of the following values: {', '.join(valid_strengths)}")
        return strength

    def __repr__(self):
        return f'<HeroPower {self.id}>'
