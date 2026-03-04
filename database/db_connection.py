import mysql.connector
#from utils.config_reader import get_config
from utils.config_reader import get_config





def connect_db():
    config = get_config()

    connection = mysql.connector.connect(
        host=config["DB"]["host"],
        user=config["DB"]["user"],
        password=config["DB"]["password"],
        database=config["DB"]["database"],
        use_pure=True
    )

    return connection
