# my-store

Just a trainy store project.

#### Stack:

- [Python](https://www.python.org/downloads/)
- [Django](https://www.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [PostgreSQL](https://www.postgresql.org/)

## Local Developing

All actions should be executed from the source directory of the project and only after installing all requirements.

1. Firstly, create and activate a new virtual environment:
   ```bash
   python3.9 -m venv ../venv
   source ../venv/bin/activate
   ```

2. Install packages:
   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

3. Create & prepare .env config file:
   ```bash
   DEBUG=True
   SECRET_KEY=
   DOMAIN_NAME=http://127.0.0.1:8000
   
   DATABASE_NAME=
   DATABASE_USER=
   DATABASE_PASSWORD=
   DATABASE_HOST=localhost
   DATABASE_PORT=
   
   EMAIL_HOST=smtp.yandex.com
   EMAIL_PORT=
   EMAIL_HOST_USER=
   EMAIL_HOST_PASSWORD=
   EMAIL_USE_SSL=

   # If you prefer the Stripe payment system, use the guide:
     https://stripe.com/docs/payments/checkout/fulfill-orders
   STRIPE_PUBLIC_KEY=
   STRIPE_SECRET_KEY=
   STRIPE_WEBHOOK_SECRET=
   ```

4. Run project dependencies, migrations, fill the database with the fixture data etc.:
   ```bash
   ./manage.py migrate
   ./manage.py loaddata <path_to_fixture_files>
   ./manage.py runserver
   ```
