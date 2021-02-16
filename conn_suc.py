import pymysql as db
from conn_cen import Conexion
from logger_base import logger
from dta_src_rep import Dta_src
from os import sys
from querys import Query
from succ_constructor import Connect


class ConnSuc:
    '''
    DAO (Data Acces Objet) 
    CRUD: Create-Read-Update-Delate entidad Persona
    '''
    __SELECCIONAR = 'SELECT * FROM data_source_replica'
    conexion = None
    __cursor = None
    
    @classmethod
    def seleccionar(cls):
        #logger.debug(Conexion.obtenerConexion())
        cursor = Conexion.obtenerCursor()
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
        #Conexion.cerrar()
        return sucursales
    
    @classmethod
    def server(cls):
        server = cls.seleccionar()
        lis_con = []
        for i in server:
            logger.debug(i.server)
            
    @classmethod
    def crearConexion(cls):
        sucursales = cls.seleccionar()
        lis_con = []
        for sucursal in sucursales:
            if sucursal.central == True:
                pass
            elif sucursal.activa == True:
                SERVER = sucursal.server
                HOST = sucursal.ip
                USER = sucursal.username
                PASSWORD = sucursal.password
                DB_NAME = 'siipapx'
                if cls.conexion is None:
                    try:
                        conexion = db.connect(HOST, USER, PASSWORD,
                                              DB_NAME)
                        lis_con.append(conexion)
                    except Exception as e:
                        logger.error(f'OCURRIO EN ERROR --> {e}')
                        pass
            else:
                logger.error(f'ERROR AL CREAR OBJETO CONEXION{SERVER}')
                pass

        return lis_con
    
    @classmethod
    def obtenerCursor(cls):
        if cls.__cursor is  None:    
            conexionesSuc = cls.crearConexion()     
            cursoresSuc = []  
            for i in conexionesSuc:
                cursor = i.cursor()
                cursoresSuc.append(cursor)
            return cursoresSuc
        else:
            return conexionesSuc

if __name__ == '__main__':
    #print('HOLA MUNDO')
    #logger.info(listaCursores)
    #logger.debug(ConnSuc.crearConexion())
    ConnSuc.server()
