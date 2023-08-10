import configparser


def get_config():
    config = configparser.ConfigParser()
    config.read('utilities/properties.ini')
    return config


def get_password():
    password = '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'
    return password
