## Setting up the environment
### 1. Provide the services
The app will require a SQL-based server: `MySQL`, `PostgreSQL` or `SQLite`. The type of dialect and database configuration can be set through environment variables:
- `DB_DIALECT`, default=`mysql`
- `DB_USERNAME`, default=`root`
- `DB_PASSWORD`, unset by default
- `DB_HOST`, default=`127.0.0.1`
- `DB_PORT`, default=`3306`

You can export each of these variables or add them to a `.env` file.
### 2. Create a virtualenv
    mkvirtualenv student-api -p python3
### 3. Install dependencies
    make requirements
### 4. Connect to database
    make database-connection
### 5. Run app locally
    make run mode=development

## To Do
- **create docker to abstract services from OS**
- **add cache**
