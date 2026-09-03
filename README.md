# Task Management Application

A Django-based task management application designed to evolve from a simple CRUD application into a production-oriented backend system.

The project currently provides user authentication and personal task management, with an ongoing focus on code quality, testing, architecture, security, and production readiness.

## Features

### Authentication

* User registration
* User login and logout
* Django authentication system
* Password validation
* User-specific task access

### Task Management

* Create tasks
* Mark tasks as completed/incomplete
* Delete tasks
* Set task deadlines
* Filter tasks by status
* Tasks are associated with the authenticated user

### Current Technology Stack

* **Python 3.11**
* **Django 4.2**
* **Django ORM**
* **SQLite** for the current development environment
* **Bootstrap 5**
* **Docker**
* **Docker Compose**

## Project Structure

```text
mysite/
├── manage.py
├── mysite/
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── user/
│   ├── migrations/
│   ├── templates/
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── docker-compose.yml
├── Dockerfile
├── manage.py
└── requirements.txt
```

## Getting Started

### Prerequisites

* Python 3.11+
* Docker
* Docker Compose

### Run with Docker

Clone the repository and start the application:

```bash
docker compose up --build
```

The application will be available at:

```text
http://localhost:8000
```

### Run locally

Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate
```

On Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run database migrations:

```bash
python manage.py migrate
```

Start the development server:

```bash
python manage.py runserver
```

## Development

The project uses Django migrations for database schema management.

Create migrations after model changes:

```bash
python manage.py makemigrations
```

Apply migrations:

```bash
python manage.py migrate
```

Create an administrator account:

```bash
python manage.py createsuperuser
```

The Django admin interface is available at:

```text
http://localhost:8000/admin/
```

## Testing

Automated tests are part of the planned development process.

Run the Django test suite with:

```bash
python manage.py test
```

As the project evolves, the test suite will be expanded to cover authentication, permissions, task management, API endpoints, validation, and edge cases.

## Roadmap

The project is intentionally being developed incrementally with a focus on production-oriented engineering practices.

### Code Quality

* [ ] Refactor existing views and forms
* [ ] Remove legacy/commented-out code
* [ ] Improve naming and project structure
* [ ] Add type hints
* [ ] Add linting and formatting
* [ ] Add pre-commit hooks

### Testing

* [ ] Add unit tests
* [ ] Add integration tests
* [ ] Add authentication and authorization tests
* [ ] Add test coverage reporting

### Security & Configuration

* [ ] Move secrets and configuration to environment variables
* [ ] Add production Django settings
* [ ] Review authentication and authorization
* [ ] Replace unsafe state-changing GET requests with POST/DELETE operations
* [ ] Add security-focused configuration

### Database & Infrastructure

* [ ] Replace SQLite with PostgreSQL
* [ ] Improve Docker configuration
* [ ] Add health checks
* [ ] Separate development and production configuration

### REST API

* [ ] Introduce Django REST Framework
* [ ] Add versioned API endpoints
* [ ] Add serializers and API validation
* [ ] Add filtering, ordering and pagination
* [ ] Add API authentication and permissions
* [ ] Add OpenAPI documentation

### Asynchronous Processing

* [ ] Introduce Redis
* [ ] Introduce Celery
* [ ] Add scheduled task processing
* [ ] Add deadline/reminder notifications

### CI/CD & Production

* [ ] Add GitHub Actions
* [ ] Run tests and linting automatically
* [ ] Build Docker images in CI
* [ ] Add deployment pipeline
* [ ] Add structured logging
* [ ] Add application health checks
* [ ] Add monitoring and error tracking


## Project Status

The application is under active development.

The initial version started as a simple Django task management application. The current goal is to progressively evolve it into a maintainable, tested, secure, and production-oriented backend system.
