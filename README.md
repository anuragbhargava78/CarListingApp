User Stories for Karan's MVP Django Application:

As a user, I want to be able to view a list of available cars on the home page.

As a user, I want to be able to filter the list of cars by make and year.

As a user, I want to be able to click on a "Buy" button next to each car listing to express my interest in purchasing that car.

As a user, I want to be able to fill out a buy form with my name and mobile number to initiate the buying process.

As a user, after submitting the buy form, I want to see a success page confirming my submission.

As a user, I want Karan to be notified via email with the details of the car, seller, sale price, and my contact information when I submit the buy form.

As a user, I want to see a "SOLD" label next to a car listing if it has been marked as sold.

As a user, I want pagination on the car listing page to navigate through multiple pages of car listings.

Karan Access:

Karan add a car for sell with help of List Car page which is located in menu.

Instructions for setting up the Django application locally:

Install Python:

Make sure Python is installed on your machine. You can download the latest version of Python from the official Python website: https://www.python.org/downloads/
Create a virtual environment (optional):

It is recommended to create a virtual environment to keep your project dependencies isolated. Open a terminal/command prompt and navigate to your project directory.
Run the following command to create a virtual environment:
python -m venv env

Install Django:
With your virtual environment activated, install Django by running the following command:
pip install Django

Set up the Django project:
Create a new Django project by running the following command:
django-admin startproject carlisting
Navigate to the project directory:
cd carlisting

Create a new Django app:
Create a new Django app within the project by running the following command:
python manage.py startapp carapp


Run the following commands to create and apply database migrations:
python manage.py makemigrations
python manage.py migrate
Create Django superuser (admin):

Create a superuser to access the Django admin site by running the following command:
python manage.py createsuperuser


Start the Django development server by running the following command:
python manage.py runserver

Access the application:
Open a web browser and navigate to http://localhost:8000 to access the home page of the Django application.
