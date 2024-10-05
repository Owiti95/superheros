from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///superheroes.db'
db = SQLAlchemy(app)
migrate = Migrate(app, db)

@app.route('/')
def index():
    return jsonify({"message": "Welcome to the Superhero API"})

if __name__ == '__main__':
    app.run(debug=True)

# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate
# from main import *

# app = Flask(__name__)

# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///superheroes.db'
# app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


# db = SQLAlchemy(app)
# migrate = Migrate(app, db)

# @app.route('/')
# def index():
#     return jsonify({"message": "superhero API"})

# if __name__ == '__main__':
#     app.run(debug=True)