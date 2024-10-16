from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Import models here
from .hero import Hero
from .heropower import HeroPower
from .power import Power
