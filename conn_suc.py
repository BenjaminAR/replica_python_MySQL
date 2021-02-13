import pymysql as db
from conn_cen import Conexion
from logger_base import logger
from dta_src_rep import Dta_src
from os import sys
from querys import Query

SELECCIONAR = 'SELECT * FROM data_source_replica'


class connSuc:
    '''
    DAO (Data Acces Objet) 
    CRUD: Create-Read-Update-Delate entidad Persona
    '''
    __SELECCIONAR = 'SELECT * FROM data_source_replica'

    @classmethod
    def seleccionar(cls):
        cursor = Conexion.obtenerCursor()
        #logger.debug(cursor.mogrify(cls.__SELECCIONAR))
        cursor.execute(cls.__SELECCIONAR)
        registros = cursor.fetchall()
        sucursales = []
        for registro in registros:
            sucursal = Dta_src(registro[0], registro[1],
                        registro[2], registro[3],
                        registro[4], registro[5],
                        registro[6], registro[7],
                        registro[8], registro[9],
                        registro[10], registro[11])
            sucursales.append(sucursal)
        Conexion.cerrar()
        return sucursales
    
    @classmethod
    def usarConexion(cls):
        sucursales = cls.seleccionar()
        for sucursal in sucursales:
            if sucursal.central == True:
                pass
            elif sucursal.activa == True:
                #logger.info(f'A replicar {sucursal.server}')
                HOST = sucursal.ip
                USER = sucursal.username
                PASSWORD = sucursal.password
                DB_NAME = 'siipapx'
                conexion = None
                cursor = None
                if conexion is None:
                    try:
                        conexion = db.connect(HOST, USER, PASSWORD,
                                              DB_NAME)
                        print(conexion)
                        logger.debug(f'Creacion de conexion con: {sucursal.server}')
                        cursor = conexion.cursor()
                        cursor.execute(Query.solDep())
                        res = cursor.fetchall()
                        if res == ():
                            logger.info('SIN DATOS NUEVOS')
                            conexion.close()
                        else:
                            logger.info(res)
                            conexion.close()
                    except Exception as e:
                        logger.error(f'OCURRIO EN ERROR --> {e}')
                        sys.exit()
            else:
                logger.error(f'ERROR AL CONTACTAR {sucursal.server}')
                pass

    
connSuc.usarConexion()
