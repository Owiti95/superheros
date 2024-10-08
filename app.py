from flask import Flask, jsonify, request#importing Flask, jsonify for JSON responses, and request for handling requests
from flask_sqlalchemy import SQLAlchemy#for database interaction
from flask_migrate import Migrate#handling database migrations

app = Flask(__name__)#initialising the Flask app
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///superheroes.db'#configuring the database
db = SQLAlchemy(app)#initialising the SQLAlchemy object with the app
migrate = Migrate(app, db)# initialising Flask-Migrate for handling database migrations

#basic route that returns a welcome message in JSON format
@app.route('/')
def index():
    return jsonify({"message": "Welcome to the Superhero API"})


# running the app in debug mode
if __name__ == '__main__':
    app.run(debug=True)

