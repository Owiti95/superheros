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



# from flask import request, jsonify
# from app import app, db
# from models import Hero, Power, HeroPower

# # Route for getting all heroes
# @app.route('/heroes', methods=['GET'])
# def get_heroes():
#     # Query the database for all heroes
#     heroes = Hero.query.all()
#     # Convert each hero to JSON format
#     json_heroes = list(map(lambda x: x.to_json(), heroes))
#     # Return the list of heroes in JSON format
#     return jsonify({"heroes": json_heroes})

# # Route for getting a specific hero by ID
# @app.route('/heroes/<int:id>', methods=['GET'])
# def get_hero(id):
#     # Query the database for the hero with the provided ID
#     hero = Hero.query.get(id)
#     if hero:
#         # Convert the hero to JSON format if found
#         return jsonify({"hero": hero.to_json()})
#     # Return an error message if the hero is not found
#     return jsonify({"error": "Hero not found"}), 404

# # Route for getting all powers
# @app.route('/powers', methods=['GET'])
# def get_powers():
#     # Query the database for all powers
#     powers = Power.query.all()
#     # Convert each power to JSON format
#     json_powers = list(map(lambda x: x.to_json(), powers))
#     # Return the list of powers in JSON format
#     return jsonify({"powers": json_powers})

# # Route for getting a specific power by ID
# @app.route('/powers/<int:id>', methods=['GET'])
# def get_power(id):
#     # Query the database for the power with the provided ID
#     power = Power.query.get(id)
#     if power:
#         # Convert the power to JSON format if found
#         return jsonify({"power": power.to_json()})
#     # Return an error message if the power is not found
#     return jsonify({"error": "Power not found"}), 404

# # Route for updating a power's description
# @app.route('/powers/<int:id>', methods=['PATCH'])
# def update_power(id):
#     # Query the database for the power with the provided ID
#     power = Power.query.get(id)
#     if power:
#         # Parse the JSON data from the request body
#         data = request.get_json()
#         # Update the power's description with the provided value
#         if 'description' in data:
#             power.description = data['description']
#             db.session.commit()  # Commit the changes to the database
#             # Return the updated power in JSON format
#             return jsonify({"power": power.to_json()})
#         # Return an error message if no description is provided
#         return jsonify({"error": "No description provided"}), 400
#     # Return an error message if the power is not found
#     return jsonify({"error": "Power not found"}), 404

# # Route for creating a new hero-power relationship (hero gains a power)
# @app.route('/hero_powers', methods=['POST'])
# def create_hero_power():
#     # Parse the JSON data from the request body
#     data = request.get_json()

#     # Check if the necessary fields are present
#     strength = data.get('strength')
#     power_id = data.get('power_id')
#     hero_id = data.get('hero_id')

#     # Validate that the necessary fields were provided
#     if not all([strength, power_id, hero_id]):
#         return jsonify({"error": "Missing required fields"}), 400

#     # Query the database for the corresponding hero and power
#     hero = Hero.query.get(hero_id)
#     power = Power.query.get(power_id)

#     if hero and power:
#         # Create a new HeroPower entry with the provided data
#         hero_power = HeroPower(strength=strength, hero_id=hero.id, power_id=power.id)
#         db.session.add(hero_power)  # Add the new entry to the database session
#         db.session.commit()  # Commit the session to save the entry

#         # Return a success message with the created hero-power relationship
#         return jsonify({"message": "Hero power created successfully", "hero_power": hero_power.to_json()}), 201
#     # Return an error message if the hero or power does not exist
#     return jsonify({"error": "Hero or Power not found"}), 404

# if __name__ == "__main__":
#     with app.app_context():
#         db.create_all()
#     app.run(debug=True)












# from flask import request, jsonify
# from config import app, db
# from models import Hero, Power, HeroPower

# # Route for getting all heroes
# @app.route('/heroes', methods=['GET'])
# def get_heroes():
#     heroes = Hero.query.all()
#     json_heroes = list(map(lambda x: x.to_json(), heroes))
#     return jsonify({"heroes": json_heroes})

# # Route for getting hero by id
# @app.route('/heroes/<int:id>', methods=['GET'])
# def get_hero(id):
#     hero = Hero.query.get(id)
#     if hero:
#         hero_data = list(map(lambda x: x.to_json(), hero))
#         return jsonify({"hero": hero_data})
#     return jsonify({"error": "Hero not found"}), 404

# # Other routes for powers, patching powers, and hero_powers creation
