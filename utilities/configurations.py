import configparser

import mysql.connector

from mysql.connector import Error


def get_config():
    config = configparser.ConfigParser()
    config.read('..\\utilities\\properties.ini')
    return config


def get_password():
    password = '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'
    return password


def get_connection():
    try:
        connection_check = mysql.connector.connect(**connect_config)
        if connection_check.is_connected():
            print("SUCCESSFUL")
            return connection_check
    except Error as e:
        print(e)


connect_config = {
    'user': get_config()['SQL']['user'],
    'password': get_config()['SQL']['password'],
    'host': get_config()['SQL']['host'],
    'database': get_config()['SQL']['database'],
}


def get_query(query):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute(query)
    row = cursor.fetchone()
    connection.close()
    return row