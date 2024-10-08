from flask import request, jsonify
from app import app, db
from models import Hero, Power, HeroPower

# Route for getting all heroes
@app.route('/heroes', methods=['GET'])
def get_heroes():
    heroes = Hero.query.all()
    return jsonify([hero.to_dict() for hero in heroes]), 200

# Route for getting hero by id
@app.route('/heroes/<int:id>', methods=['GET'])
def get_hero(id):
    hero = Hero.query.get(id)
    if hero:
        hero_data = hero.to_dict()
        hero_data['hero_powers'] = [hp.to_dict() for hp in hero.hero_powers]
        return jsonify(hero_data), 200
    return jsonify({"error": "Hero not found"}), 404

# Route for getting all powers
@app.route('/powers', methods=['GET'])
def get_powers():
    powers = Power.query.all()
    return jsonify([power.to_dict() for power in powers]), 200

# Route for getting a power by id
@app.route('/powers/<int:id>', methods=['GET'])
def get_power(id):
    power = Power.query.get(id)
    if power:
        return jsonify(power.to_dict()), 200
    return jsonify({"error": "Power not found"}), 404

# Route for updating a power (PATCH)
@app.route('/powers/<int:id>', methods=['PATCH'])
def update_power(id):
    power = Power.query.get(id)
    if power:
        data = request.get_json()
        if 'description' in data:
            power.description = data['description']
            db.session.commit()
            return jsonify(power.to_dict()), 200
        return jsonify({"error": "Invalid data"}), 400
    return jsonify({"error": "Power not found"}), 404

# Route for creating a new hero power
@app.route('/hero_powers', methods=['POST'])
def create_hero_power():
    data = request.get_json()
    
    strength = data.get('strength')
    power_id = data.get('power_id')
    hero_id = data.get('hero_id')
    
    if not strength or not power_id or not hero_id:
        return jsonify({"error": "Missing required fields"}), 400

    # Check if hero and power exist
    hero = Hero.query.get(hero_id)
    power = Power.query.get(power_id)
    
    if not hero or not power:
        return jsonify({"error": "Hero or Power not found"}), 404

    # Create new hero power entry
    hero_power = HeroPower(strength=strength, power_id=power_id, hero_id=hero_id)
    db.session.add(hero_power)
    db.session.commit()

    return jsonify(hero_power.to_dict()), 201

