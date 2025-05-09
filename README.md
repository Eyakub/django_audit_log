# Django Audit Log Demo

This project demonstrates the usage of django-easy-audit to track various types of activities in a Django application, including:
- REST API requests
- GraphQL queries and mutations
- Django Admin actions
- Model changes
- User authentication events
- User agent and country information

## Features

- Task management system with REST API and GraphQL endpoints
- audit logging
- User authentication
- Django Admin interface
- GeoIP tracking for country information

## Setup

### Option 1: Local Development

1. Create and activate a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up GeoIP database:
```bash
# Run the GeoIP setup script
python download_geoip.py

# Follow the instructions to download and extract the GeoIP databases
```

4. Run migrations:
```bash
python manage.py migrate
```

5. Create a superuser:
```bash
python manage.py createsuperuser
```

6. Run the development server:
```bash
python manage.py runserver
```

### Option 2: Docker Setup

1. Set up GeoIP database:
```bash
# Run the GeoIP setup script
python download_geoip.py

# Follow the instructions to download and extract the GeoIP databases
```

2. Build and start the containers:
```bash
docker-compose up --build
```

3. In a new terminal, create a superuser:
```bash
docker-compose exec web python manage.py createsuperuser
```

4. The application will be available at:
- Django Admin: http://localhost:8000/admin/
- REST API: http://localhost:8000/api/
- GraphQL: http://localhost:8000/graphql/


## Audit Log Features

The project tracks:
- All REST API requests
- GraphQL queries and mutations
- Model changes (create, update, delete)
- User login/logout events
- User agent information
- Country information (requires GeoIP2 database)

## Testing the Audit Log

1. Log in to the Django Admin interface
2. Create/update/delete tasks through the admin interface
3. Use the REST API to manage tasks
4. Use GraphQL to manage tasks
5. Check the audit logs in the Django Admin interface under "Easy Audit" section
   - You'll see country information for each request
   - User agent information is also tracked
   - IP addresses are logged

## GeoIP Setup

To enable country tracking:

1. Sign up for a free MaxMind account at https://www.maxmind.com/en/geolite2/signup
2. Download the GeoLite2 databases:
   - GeoLite2-Country.tar.gz
   - GeoLite2-City.tar.gz
3. Place the downloaded files in the `geoip` directory
4. Run the setup script:
```bash
python download_geoip.py
```

The script will extract the necessary database files and clean up the downloaded archives.
