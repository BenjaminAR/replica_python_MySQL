from datetime import date
from datetime import datetime

class Query:
    today = date.today()
    __SOL_DEP = f"SELECT * FROM solicitud_de_deposito WHERE cobro_id IS NULL AND DATE(fecha) >='{today}' and version >=1 LIMIT 10"
    __CLIENTE = "SELECT * FROM cliente LIMIT 10"
    __COM_EMPRESA = 'SELECT * FROM comunicacion_empresa LIMIT 1'
    __SELECCIONAR = 'SELECT * FROM data_source_replica'
    
    @classmethod
    def selSuc(cls):
        return cls.__SELECCIONAR
    
    
    @classmethod
    def solDep(cls):
        return cls.__SOL_DEP

    @classmethod
    def cliente(cls):
        return cls.__CLIENTE
    
    @classmethod
    def comEmp(cls):
        return cls.__COM_EMPRESA
        

if __name__ == '__main__':
    print(Query.solDep())
    print(Query.cliente())
    print(Query.comEmp())
