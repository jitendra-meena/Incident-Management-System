# Incident Management System

The Incident Management System is a REST API-based application that allows users to create and manage incidents.

## Requirements

- Ubuntu (Preferred)
- Python 3.6 and above
- MySQL (Preferred)
- Django 3.x
- Django Rest Framework (DRF)
- django-filter
- Postman (for testing the APIs)

## Installation

1. Clone the repository:

   ```shell
   git clone <repository-url>
   cd incident-management-system
# Incident Management System

The Incident Management System is a REST API-based application that allows users to create and manage incidents.

## Requirements

- Ubuntu (Preferred)
- Python 3.6 and above
- MySQL (Preferred)
- Django 3.x
- Django Rest Framework (DRF)
- django-filter
- Postman (for testing the APIs)

## Installation

1. Clone the repository:

   ```shell
   git clone <repository-url>
   cd incident-management-system

2. Create and activate a virtual environment:
```
python -m venv env
source env/bin/activate
```

3. Create and activate a virtual environment::

python -m venv env
source env/bin/activate

4. Install the required packages:

pip install -r requirements.txt

5. Configure the database settings:

Open the settings.py file in the incidentmanagement directory.
Update the DATABASES configuration with your MySQL database settings.

6. Apply database migrations:

python manage.py migrate

7. Start the development server:

python manage.py runserver

8. The API endpoints will be available at http://localhost:8000/api/.

Usage
Register a new user by making a POST request to http://localhost:8000/api/register/. Provide the username and password in the request body.

Log in with a user by making a POST request to http://localhost:8000/api/login/. Provide the username and password in the request body. The response will include an authentication token.

Use the provided authentication token in the Authorization header for subsequent requests. Example: Authorization: Token <token>.

Create incidents by making a POST request to http://localhost:8000/api/incidents/. Provide the incident details in the request body, including reporter name, incident details, priority, and status.

View incidents created by the logged-in user by making a GET request to http://localhost:8000/api/incidents/.

Update an incident by making a PATCH or PUT request to http://localhost:8000/api/incidents/<incident-id>/. Provide the updated incident details in the request body.

Search for incidents using the incident ID by making a GET request to http://localhost:8000/api/incidents/?incident_id=<incident-id>.

Only the creator of an incident can edit or delete it. Other users cannot access or modify incidents created by other users.
