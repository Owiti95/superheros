# Superhero API

This project is a simple Flask API for managing superheroes and their powers. It allows users to create, retrieve, and update heroes, powers, and their relationships.

## Features

- Retrieve all superheroes
- Retrieve a superhero by ID
- Retrieve all powers
- Retrieve a power by ID
- Update a power's description
- Create a relationship between a superhero and a power (HeroPower)

## Technologies Used

- **Flask**: A lightweight WSGI web application framework.
- **Flask-SQLAlchemy**: An ORM (Object Relational Mapper) for Flask to handle database operations.
- **Flask-Migrate**: Handles database migrations.
- **SQLite**: A lightweight database for development.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/superhero-api.git
    cd superhero-api
    ```

2. Create a virtual environment and activate it:

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Set up the database:

    ```bash
    flask db init
    flask db migrate
    flask db upgrade
    ```

5. Run the application:

    ```bash
    flask run
    ```

6. The application will be available at `http://127.0.0.1:5000`.

## API Endpoints

### Heroes

- **GET /heroes**: Retrieve a list of all heroes.
  
    **Response:**
    ```json
    [
      {
        "id": 1,
        "name": "Clark Kent",
        "super_name": "Superman"
      }
    ]
    ```

- **GET /heroes/:id**: Retrieve a specific hero by ID.
  
    **Response:**
    ```json
    {
      "id": 1,
      "name": "Clark Kent",
      "super_name": "Superman",
      "hero_powers": [
        {
          "id": 1,
          "strength": "Strong",
          "power_id": 1,
          "hero_id": 1,
          "power": {
            "id": 1,
            "name": "Flight",
            "description": "Ability to fly"
          }
        }
      ]
    }
    ```

### Powers

- **GET /powers**: Retrieve a list of all powers.
  
    **Response:**
    ```json
    [
      {
        "id": 1,
        "name": "Flight",
        "description": "Ability to fly"
      }
    ]
    ```

- **GET /powers/:id**: Retrieve a specific power by ID.
  
    **Response:**
    ```json
    {
      "id": 1,
      "name": "Flight",
      "description": "Ability to fly"
    }
    ```

- **PATCH /powers/:id**: Update a power's description.

    **Request Body:**
    ```json
    {
      "description": "Super speed in the air"
    }
    ```

    **Response:**
    ```json
    {
      "id": 1,
      "name": "Flight",
      "description": "Super speed in the air"
    }
    ```

### Hero Powers

- **POST /hero_powers**: Create a new relationship between a hero and a power.
  
    **Request Body:**
    ```json
    {
      "strength": "High",
      "hero_id": 1,
      "power_id": 1
    }
    ```

    **Response:**
    ```json
    {
      "id": 1,
      "strength": "High",
      "hero_id": 1,
      "power_id": 1,
      "hero": {
        "id": 1,
        "name": "Clark Kent",
        "super_name": "Superman"
      },
      "power": {
        "id": 1,
        "name": "Flight",
        "description": "Ability to fly"
      }
    }
    ```

## Database Models

### Hero

| Column   | Type     | Description       |
|----------|----------|-------------------|
| id       | Integer  | Primary key       |
| name     | String   | Hero's real name  |
| super_name | String   | Hero's superhero name |

### Power

| Column   | Type     | Description     |
|----------|----------|-----------------|
| id       | Integer  | Primary key     |
| name     | String   | Name of the power |
| description | String | Power description |

### HeroPower

| Column   | Type     | Description       |
|----------|----------|-------------------|
| id       | Integer  | Primary key       |
| strength | String   | Strength level    |
| hero_id  | Integer  | Foreign key for the Hero |
| power_id | Integer  | Foreign key for the Power |

## Future Enhancements

- Add authentication for managing heroes and powers.
- Implement filtering and searching for heroes by power or strength.
- Add support for pagination when retrieving large lists of heroes or powers.