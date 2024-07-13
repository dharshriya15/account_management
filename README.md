# Django REST API for Account and Destination Management

This Django web application provides a RESTful API for managing accounts and destinations, along with a data receiving endpoint.

## Features

- CRUD operations for Accounts
- CRUD operations for Destinations
- Retrieval of destinations for a specific account
- Secure data receiving endpoint

## API Endpoints

### Accounts

- `GET /api/accounts/`: List all accounts
- `POST /api/accounts/`: Create a new account
- `GET /api/accounts/<id>/`: Retrieve a specific account
- `PUT /api/accounts/<id>/update`: Update a specific account
- `DELETE /api/accounts/<id>/delete`: Delete a specific account

### Destinations

- `GET /api/destinations/`: List all destinations
- `POST /api/destinations/`: Create a new destination
- `GET /api/destinations/<id>/`: Retrieve a specific destination
- `PUT /api/destinations/<id>/update`: Update a specific destination
- `DELETE /api/destinations/<id>/delete`: Delete a specific destination

### Account Destinations

- `GET /api/accounts/<id>/destinations/`: Get destinations for a specific account

### Data Receiving

- `POST /server/incoming_data`: Receive and process incoming data

## Data Receiving Endpoint

The `/server/incoming_data` endpoint accepts POST requests with JSON data and an app secret token. It processes the data and forwards it to the appropriate destinations based on the account associated with the secret token.

### Requirements

- POST method only
- JSON format data
- Valid app secret token

### Error Responses

- "Invalid Data": Returned for GET requests or non-JSON data
- "Un Authenticate": Returned when the app secret token is missing or invalid

## Installation

1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Apply migrations: `python manage.py migrate`
4. Run the server: `python manage.py runserver`
