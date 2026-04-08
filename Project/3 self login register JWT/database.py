import mysql.connector
import os

def database():
    return mysql.connector.connect(
        host = os.getenv('host'),
        user = os.getenv('user'),
        password = os.getenv('password'),
        database = os.getenv('db')
    )

