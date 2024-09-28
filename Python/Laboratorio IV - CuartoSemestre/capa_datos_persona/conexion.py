
from logger_base import log
import sys
from psycopg2 import pool
class Conexion:
    _DATABASE = 'test_BD'
    _USERNAME = 'postgres'
    _PASSWORD = 'root'
    _DB_PORT = '5432'
    _HOST = '127.0.0.1'
    _MIN_CON = 1
    _MAX_CON = 5
    _pool = None
    
    """ _conexion = None
    _cursor = None """
    
    @classmethod
    def obtenerConexion(cls):
        """ if cls._conexion is None:
            try:
                cls._conexion = bd.connect(host=cls._HOST,
                                           user=cls._USERNAME,
                                           password=cls._PASSWORD,
                                           port=cls._DB_PORT,
                                           database=cls._DATABASE)
                log.debug(f'Conexion Exitosa: {cls._conexion}')
                return cls._conexion
            except Exception as e:
                log.error(f'Ocurrio un error de tipo: {e}')
                sys.exit()
        else:
                return cls._conexion """
        conexion = cls.obtenerPool().getconn()
        log.debug(f'conexion obtenida del pool: {conexion}')
        return conexion
    
            
    @classmethod
    def obtenerCursor(cls):
        """ if cls._cursor is None:
            try:
                cls._cursor = cls.obtenerConexion().cursor()
                log.debug(f'se abrio correctamente el cursor: {cls._cursor}')
                return cls._cursor
            except Exception as e:
                log.error(f'Ocurrio un error: {e}')
                sys.exit()
            else:
                return cls._cursor """
        pass
    @classmethod
    def obtenerPool(cls):
        if cls._pool is None:
            try:
                cls._pool = pool.SimpleConnectionPool(cls._MIN_CON,
                                                      cls._MAX_CON,
                                                      host=cls._HOST,
                                                      user=cls._USERNAME,
                                                      password=cls._PASSWORD,
                                                      port=cls._DB_PORT,
                                                      database = cls._DATABASE)
                log.debug(f'cracion del pool exitosa: {cls._pool}')
                return cls._pool
            except Exception as e:
                log.error(f'Ocurrio un error alobtener el pool: {e}')
                sys.exit()
        else:
            return cls._pool
    @classmethod
    def liberarConexion(cls, conexion):
        cls.obtenerPool().putconn(conexion)
        log.debug(f'regresamos la conexion del pool: {conexion}')
    
    @classmethod 
    def cerrarConexiones(cls):
        cls.obtenerPool().closeall()
        log.debug(f'se cerraron todas las conexiones')

if __name__ == '__main__':
    conexion1 = Conexion.obtenerConexion()
    Conexion.liberarConexion(conexion1)
    conexion2 = Conexion.obtenerConexion()
    conexion3 = Conexion.obtenerConexion()
    Conexion.liberarConexion(conexion2)
    Conexion.liberarConexion(conexion3)
    conexion4 = Conexion.obtenerConexion()
    conexion5 = Conexion.obtenerConexion()
    conexion6 = Conexion.obtenerConexion()
        
