# System Requirements
=================================
* Python >= 3.6 
* sqlite

# Setup
1.  Create a virtual environment.
    * `$ python3.6 -m venv env3`
2.  Activate the virtual environemnt.
    * `$ source env3/bin/activate`
3.  Upgrade pip installation.
    * `$ pip install --upgrade pip`
4.  Install python packages via pip.
    * `$ pip install -r requirements.txt`
5.  Move into the django project directory.
    * `$ cd python_projects_api`
6.  Execute django database migrations.
    * `$ python manage.py migrate`
7.  Start the django_restframework server.
    * `$ python manage.py runserver`

# Endpoint Descriptions
There are three endpoints associated with this application.

1.  The first endpoint is the `projects` endpoint.  It is located at
`localhost:8000/projects`.  This lists all the projects ingested into the
sqlite database.  If the server has not executed an ingest routine, this page
will return an empty dictionary.  This endpoint allows you to order the results
by name, stars, creation time, and last push time.  The default ordering is
descending by stars.
2.  The second endpoint displays all information for a record identified by its
primary key.  It is accessed as `localhost:8000/projects/<pk>`.
3.  The final endpoint updates the database with a put method. When the put is
triggered, the ingest script is called and the data is serialized by the
serializer method to update or create objects as needed.  You must visit this
endpoint at least once with a PUT method to trigger the ingest process.

# Architecture Notes
This follows the django application architecture allowing multiple apps to be created
within a single settings management project.  The project application logic is
defined in `drf_github_stars/python_projects_api/python_projects` directory.
The `models` module defines the database tables.  The `apiviews` module defines displaying
model information to the user and retrieving updates from the user.  This is where
CRUD operations are controlled.  The `serializer` module handles data validation.
The `urls` module maps endpoints to the data view.