import os
import mysql.connector

def database():
    return mysql.connector.connect(
        host = os.getenv('host'),
        user = os.getenv('user'),
        password = os.getenv('password'),
        database = os.getenv('database')
    )