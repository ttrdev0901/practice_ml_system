import configparser

config = configparser.ConfigParser()
config.read("..\settings\config.ini")

def read_db_config():
    """データベースの設定を読み込んでdictで返す関数
    """
    return dict(config['database'])


if __name__ == "__main__":
    pass