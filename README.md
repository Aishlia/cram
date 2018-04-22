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

## Trouble shooting

If you make changes in the Models and run into DB schema issues, delete the sqlite DB file `app.sqlite`.

