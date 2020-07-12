## Setting up the environment
### 1. Provide the services
The app will require a `MySQL` server with the following base settings:
- default username `root`
- no password
- host `127.0.0.1`
- default port `3306`
### 2. Create a virtualenv
    mkvirtualenv student-api -p python3
### 3. Install dependencies
    make requirements
### 4. Connect to database
    make database-connection

## To Do
- add Flask app with test route
- add POST, GET (list), GET(filter), PATCH and DELETE routes and views

- **create docker to abstract services from OS**
- **add cache**
