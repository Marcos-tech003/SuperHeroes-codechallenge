from app import app
from models import db, Hero, HeroPower, Power

with app.app_context():
    db.create_all()

    # Add Heroes
    hero1 = Hero(name="Clark Kent", super_name="Superman")
    hero2 = Hero(name="Bruce Wayne", super_name="Batman")
    db.session.add_all([hero1, hero2])
    db.session.commit()

    # Add Powers
    power1 = Power(name="Super Strength", description="Gives the hero the strength to lift heavy objects.")
    power2 = Power(name="Flight", description="Allows the hero to fly through the air at incredible speeds.")
    db.session.add_all([power1, power2])
    db.session.commit()

    # Add Hero Powers
    hero_power1 = HeroPower(strength="Strong", hero_id=hero1.id, power_id=power1.id)
    hero_power2 = HeroPower(strength="Weak", hero_id=hero2.id, power_id=power2.id)
    db.session.add_all([hero_power1, hero_power2])
    db.session.commit()

print("Seeding completed!")
