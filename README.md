# Sabte Shams

Sabte Shams is a Django-based accounting management system designed to help you manage your payments, expenses, statements, invoices, and rents. The application uses Persian (Farsi) language and supports Jalali dates.

## Features

- Manage payments, expenses, statements, invoices, and rents.
- Persian language support.
- Jalali date support using `django_jalali`.
- RESTful API for accessing and managing data.

## Installation

### Prerequisites

- Python 3.x
- Django 3.x or later

### Steps

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/sabte_shams.git
    cd sabte_shams
    ```

2. Create and activate a virtual environment:

    ```bash
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3. Install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Run the migrations:

    ```bash
    python manage.py migrate
    ```

5. Create a superuser:

    ```bash
    python manage.py createsuperuser
    ```

6. Start the development server:

    ```bash
    python manage.py runserver
    ```

## Usage

### Admin Panel

To access the admin panel, go to `http://127.0.0.1:8000/admin` and log in with the superuser credentials.

### API Endpoints

The following API endpoints are available:

- Payments: `http://127.0.0.1:8000/api/payments/`
- Expenses: `http://127.0.0.1:8000/api/expenses/`
- Statements: `http://127.0.0.1:8000/api/statements/`
- Invoices: `http://127.0.0.1:8000/api/invoices/`
- Rents: `http://127.0.0.1:8000/api/rents/`

Use these endpoints to interact with the accounting data programmatically.

## Tests

Run the tests to ensure everything is working correctly:

```bash
python manage.py test
