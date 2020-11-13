import configparser

def get_config(path):
    config = configparser.ConfigParser()
    config.read(path)
    return config

def get_parameter(config, section, key):
    value = str(config[section][key])
    if value.upper() == 'TRUE':
        return True
    elif value.upper() == 'FALSE':
        return False
    else:
        return value