from os import sys
import pymysql as db
from logger_base import logger
from pymysql import converters
converions = converters.conversions
converions[db.FIELD_TYPE.BIT] = lambda x: x == b'\x01' 


class Conexion:
    __HOST = '10.10.1.229'
    __USER = 'root'
    __PASSWORD = 'sys'
    __DB_NAME = 'siipapx'
    __conexion = None
    __cursor = None

    @classmethod
    def obtenerConexion(cls):
        if cls.__conexion is None:
            try:
                cls.__conexion = db.connect(cls.__HOST, cls.__USER, cls.__PASSWORD,
                                            cls.__DB_NAME)
    
                return cls.__conexion
            except Exception as e:
                logger.debug(f'Error:{e}')
                sys.exit()
        else:
            return cls.__conexion

    @classmethod
    def obtenerCursor(cls):
        if cls.__cursor is None:
            try:
                cls.__cursor = cls.obtenerConexion().cursor()
                return cls.__cursor
            except Exception as e:
                logger.debug(f'Error:{e}')
                sys.exit()
        else:
            return cls.__cursor

'''    @classmethod
    def cerrar(cls):
        if cls.__cursor is not None:
            try:
                cls.__cursor.close()
            except Exception as e:
                logger.debug(f'Error:{e}')

        if cls.__conexion is not None:
            try:
                cls.__conexion.close()
            except Exception as e:
                logger.debug(f'Error:{e}')'''


if __name__ == '__main__':
    print('--------LOCAL------------')