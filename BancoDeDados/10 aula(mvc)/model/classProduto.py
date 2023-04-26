class Produto:
    def __init__(self, dbname, host, port, user, password) -> None:
        
        self._dbname = dbname
        self._host = host
        self._port = port
        self._user = user
        self._password = password
