# arcitech-django-assignment

# CMS Project

This is a Content Management System (CMS) backend implemented with Django and Django Rest Framework (DRF).

## Features

- Admin can view, edit, and delete all contents created by multiple authors.
- Authors can create, view, edit, and delete contents created by them only.
- Users can search content by matching terms in title, body, summary, and categories.

## Requirements

- Python 3.8+
- Django Rest Framework
- SimpleJWT for token-based authentication

## Installation

1. **Clone this repository:**

2. **Create and activate a virtual environment:**

    ```bash
    python -m venv venv
    `venv\Scripts\activate`
    ```

3. **Install the dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Apply the migrations:**

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5. **Create an admin user (superuser):**

    ```bash
    python manage.py createsuperuser
    ```

6. **Run the server:**

    ```bash
    python manage.py runserver
    ```
