
## Setting up a development environment

Assuming that you have `git` and `virtualenv` and `virtualenvwrapper` installed.

    # Clone the code repository 
    git clone https://github.com/lingthio/Flask-User-starter-app.git my_app

    # Create the 'my_app' virtual environment
    mkvirtualenv -p PATH/TO/PYTHON hackathon_2018

    # Install required Python packages
    workon my_app
    pip install -r requirements.txt

## Initializing the Database

    # Create DB tables and populate the roles and users tables
    python manage.py init_db

## Running the app

    # Start the Flask development web server
    python manage.py runserver

Point your web browser to http://localhost:5000/

You can make use of the following users:
- email `user@example.com` with password `Password1`.
- email `admin@example.com` with password `Password1`.


## Running the automated tests

    # Start the Flask development web server
    py.test tests/


## Trouble shooting

If you make changes in the Models and run into DB schema issues, delete the sqlite DB file `app.sqlite`.

