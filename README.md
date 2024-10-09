# SuperHeroes-codechallenge


This project is a RESTful API built with Flask and Flask-SQLAlchemy. It tracks superheroes and their unique superpowers, following a one-to-many relationship. The project is structured to follow best practices in Python and API development.

## Features

- **Superhero management**: Add, update, delete superheroes.
- **Power management**: Add, update, delete superpowers.
- **HeroPower Assignment**: Assign powers to superheroes with additional attributes such as the hero's rating for a given power.

## Models

1. **Hero**
   - Attributes: `id`, `name`, `super_name`
   - Relationships: A hero can have many powers through the HeroPower model.

2. **Power**
   - Attributes: `id`, `name`, `description`
   - Relationships: Powers can be linked to multiple heroes through the HeroPower model.

3. **HeroPower**
   - Attributes: `id`, `strength` (values: Weak, Average, Strong), `hero_id`, `power_id`
   - Relationships: A join table to connect heroes and powers, with an additional attribute for the power's strength in the hero.

## Installation

### Prerequisites

- Python 3.8.x
- Flask
- Flask-SQLAlchemy
- Flask-Migrate
- pytest (for testing)

### Setup

1. **Clone the repository**:

   ```bash
   git clone  https://github.com/Marcos-tech003/SuperHeroes-codechallenge
   cd SuperHeroes-codechallenge

python3 -m venv venv

source venv/bin/activate  # For Linux/macOS

venv\Scripts\activate     # For Windows

pip install -r requirements.txt

flask db init
flask db migrate
flask db upgrade


python seed.py


flask run
The API will be available at http://127.0.0.1:5000.



Here's the README.md in markdown format:

markdown
Copy code
# Superheroes and Powers API

This project is a RESTful API built with Flask and Flask-SQLAlchemy. It tracks superheroes and their unique superpowers, following a one-to-many relationship. The project is structured to follow best practices in Python and API development.

## Features

- **Superhero management**: Add, update, delete superheroes.
- **Power management**: Add, update, delete superpowers.
- **HeroPower Assignment**: Assign powers to superheroes with additional attributes such as the hero's rating for a given power.

## Models

1. **Hero**
   - Attributes: `id`, `name`, `super_name`
   - Relationships: A hero can have many powers through the HeroPower model.

2. **Power**
   - Attributes: `id`, `name`, `description`
   - Relationships: Powers can be linked to multiple heroes through the HeroPower model.

3. **HeroPower**
   - Attributes: `id`, `strength` (values: Weak, Average, Strong), `hero_id`, `power_id`
   - Relationships: A join table to connect heroes and powers, with an additional attribute for the power's strength in the hero.

## Installation

### Prerequisites

- Python 3.8.x
- Flask
- Flask-SQLAlchemy
- Flask-Migrate
- pytest (for testing)

### Setup

1. **Clone the repository**:

   ```bash
   git clone https://github.com/Marcos-tech003/Phase-4-code-challenge-1.git
   cd Phase-4-code-challenge-1
Create and activate a virtual environment:

bash
Copy code
python3 -m venv venv
source venv/bin/activate  # For Linux/macOS
# or
venv\Scripts\activate     # For Windows
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Set up the database:

Initialize the database and run migrations:

bash
Copy code
flask db init
flask db migrate
flask db upgrade
Seed the database:

Run the seed.py file to populate the database with sample data:

bash
Copy code
python seed.py
Run the application:

bash
Copy code
flask run
The API will be available at http://127.0.0.1:5000.

API Endpoints
GET /heroes: Retrieve a list of all superheroes.

GET /heroes/
: Retrieve details for a specific hero.

POST /heroes: Create a new superhero.

PATCH /heroes/
: Update a specific hero's details.

DELETE /heroes/
: Remove a superhero from the database.

GET /powers: Retrieve a list of all superpowers.

GET /powers/
: Retrieve details for a specific power.

PATCH /powers/
: Update a specific power's details.

POST /heropowers: Assign a power to a superhero with a specific strength.