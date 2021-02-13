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

    def __str__(self):
        return (
            f'{self.id} '
            f'{self.version} '
            f'{self.central} '
            f'{self.username} '
            f'{self.url} '
            f'{self.server} '
            f'{self.ip} '
            f'{self.password} '
            f'{self.data_base} '
            f'{self.activa} '
            f'{self.url_alternativa} '
            f'{self.sucursal} '
        )
