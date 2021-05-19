# Backend for Dr. Machine

This application is developed using [Django](https://www.djangoproject.com/), [Django REST Framework](https://www.django-rest-framework.org/), and [Djoser](https://djoser.readthedocs.io/en/latest/getting_started.html).

## Usage
- Create a virtual environment:
    ```shell
    $ python -m venv .venv
    ```
- Activate the virtual environment:
    ```shell
    $ source .venv/bin/activate
    ```
- Install the required packages:
    ```shell
    $ pip install -r requirements.txt
    ```
- Apply Django migrations:
    ```shell
    $ python manage.py migrate
    ```
- Create a super-user:
    ```shell
    $ python manage.py createsuperuser
    ```
- Run server:
    ```shell
    $ python manage.py runserver --settings=backend.settings.development
    ```