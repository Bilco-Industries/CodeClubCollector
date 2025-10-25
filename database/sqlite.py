# This library allows us to talk to our database, we will store our temperature logs in here
import sqlite3

DATABASE_NAME = 'CodeClub.db'

# This is a mini library that will handle the interaction with the database for us
class Sqlite:
    _connection = None;

    def _connect():
        try:
            sqlite3._connect(DATABASE_NAME)
        except e:
            print

    # This function will create the tables in the database if they do not already exist
    def try_create_tables():
        