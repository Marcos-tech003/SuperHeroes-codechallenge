from app import app, db
from models.hero import Hero
from models.power import Power
from models.heropower import HeroPower

def seed_data():
    # Create heroes
    hero1 = Hero(name="Kamala Khan", super_name="Ms. Marvel")
    hero2 = Hero(name="Peter Parker", super_name="Spider-Man")
    
    # Create powers
    power1 = Power(name="Super Strength", description="Gives super-human strength.")
    power2 = Power(name="Flight", description="Gives the ability to fly.")
    
    # Create hero powers
    heropower1 = HeroPower(hero=hero1, power=power1, strength="Strong")
    heropower2 = HeroPower(hero=hero2, power=power2, strength="Average")
    
    # Add all data to the session and commit
    db.session.add_all([hero1, hero2, power1, power2, heropower1, heropower2])
    db.session.commit()

if __name__ == '__main__':
    with app.app_context():  
        seed_data()
        print("Seeding completed!")
