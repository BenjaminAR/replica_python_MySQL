import logging
# Variable logger a utilizar
logger = logging

logger.basicConfig(level=logging.DEBUG,
                   format='%(asctime)s: %(levelname)s [%(filename)s, %(lineno)s] %(message)s',
                   datefmt='%D -> %I:%M %p',
                   handlers=[
                       logging.FileHandler('capa_datos.log'),
                       logging.StreamHandler()
                   ])

if __name__ == '__main__':
    logging.warning(' Mensaje a nivel warning')
    logging.info(' Mensje a nivel info')
    logging.debug(' Mensaje a nivel debug')
    logging.error('Ocurrio un error en la base de datos')
