from conn_suc import ConnSuc
from conn_cen import Conexion
from logger_base import logger
from querys import Query
 
class obtenerQuery:
    
    @classmethod
    def resCen(cls):
        cursor = Conexion.obtenerCursor()
        cursor.execute(Query.solDep())
        registros = cursor.fetchall()
        registrosCen = []
        for registro in registros:
            registrosCen.append(registros)
        return registrosCen
    
    @classmethod
    def resSuc(cls):
        cursores = ConnSuc.obtenerCursor()
        #server =  ConnSuc.server()
        registrosSuc = []
        for u in cursores:
            u.execute(Query.solDep())
            registros = u.fetchall()
            if registros == ():
                pass
            else:
                print('\n\n')
                registrosSuc.append(registros)
        return registrosSuc
            
       
if __name__ == '__main__': 
    #logger.info(ConnSuc.obtenerCursor())   
    uno = obtenerQuery.resCen()
    print('\n\n')
    dos = obtenerQuery.resSuc()
    print(uno)
    print('----------------------------------------------------')
    print(dos)