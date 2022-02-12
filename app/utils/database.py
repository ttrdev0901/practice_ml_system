from app.utils import config_reader

def get_db_url() -> str:
    """DBへの接続URLを返す関数

    Returns
    -------
    str
        接続URL, 
        postgresql+<connector>://username:password@<hostname>:port/dbname
    """
    db = config_reader.read_db_config()
    return ("postgresql+{connector}://"
            "{username}:{password}@{hostname}:{port}/{dbname}").format(**db)

