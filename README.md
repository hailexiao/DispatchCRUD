## Dispatch exercise
This is a webapp to create, read, update, and delete companies to and from a SQLite3 datastore. All markup is rendered server-side.

## Instructions
* Clone the git repository to a local directory
* Make sure you have Python > 3.6 installed, and create a virtual environment in the directory:

```python3 -m venv /path/to/directory```
* Install and run SQLite3, and create a DB using the following command:

```.open /path/to/directory```
* Run migrations to get the latest version of the DB schema:

```flask db upgrade```
* Run the app:

```flask run```
