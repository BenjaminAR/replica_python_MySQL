from logger_base import logger

class Dta_src:
    def __init__(self, id, version, central, username, url, server, ip, password, 
                 data_base, activa, url_alternativa, sucursal):
        self.id = id
        self.version = version
        self.central = central
        self.username = username
        self.url = url
        self.server = server
        self.ip = ip
        self.password = password
        self.data_base = data_base
        self.activa = activa
        self.url_alternativa = url_alternativa
        self.sucursal = sucursal
