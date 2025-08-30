import configparser



def getConfig():
    config = configparser.ConfigParser()
    config.read('utils/config.ini')
    return config
