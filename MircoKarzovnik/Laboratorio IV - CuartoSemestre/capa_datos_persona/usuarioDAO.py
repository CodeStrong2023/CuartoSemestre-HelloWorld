from conexion import Conexion
from Persona import Persona
from logger_base import log
from cursor_del_pool import CursorDelPool
from usuario import Usuario

class UsuarioDao:
    
    ''' 
    DAO significa: Data Access Object
    CRUD significa:
        creaate -> insertar
        read -> seleccionar
        update -> actualizar
        delte -> eliminar
    '''
    _SELECCIONAR = 'SELECT * FROM usuario ORDER BY id_usuario'
    _INSERTAR = 'INSERT INTO usuario(username, password) VALUES (%s,%s)'
    _ACTUALIZAR = 'UPDATE usuario SET username=%s, password=%s WHERE id_usuario=%s'
    _ELIMINAR = 'DELETE FROM usuario WHERE id_usuario=%s'
        
    #definimos los metodos de la clase
    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            usuarios=[]
            for registro in registros:
                usuario = Persona(registro[0],registro[1],registro[2])
                usuarios.append(usuario)
            return usuarios
    @classmethod
    def insertar(cls, usuario):
        with CursorDelPool() as cursor:
            valores = (usuario.username,usuario.password)
            cursor.execute(cls._INSERTAR,valores)
            log.debug(f'Usuario a insertar: {usuario}')
            return cursor.rowcount 
    @classmethod
    def actualizar(cls, usuario):  
        with CursorDelPool() as cursor:
            valores = (usuario.username, usuario.password, usuario.id_usuario)
            cursor.execute(cls._ACTUALIZAR,valores)
            log.debug(f'Usuario actualizado: {usuario}')
            return cursor.rowcount 
    @classmethod
    def eliminar(cls, usuario):
        with CursorDelPool() as cursor:
            valores=(usuario.id_usuario,)
            cursor.execute(cls._ELIMINAR,valores)
            log.debug(f'los usuarios eliminados son: {usuario}')
            return cursor.rowcount
        
        
if __name__ == '__main__':
    """ #insertar usuario
    usuario1 = Usuario(username='leugenio',password='2625')
    usuario_insertado = UsuarioDao().insertar(usuario1)
    log.debug(f'usuario insertado: {usuario1}') """
    #Actualiza usuario
    usuario1 = Usuario(id_usuario=2,username='leito',password='2189')
    usuario_actualizado = UsuarioDao.actualizar(usuario1)
    #Eliminar usuario
    usuario2 = Usuario(id_usuario=2)
    borrar_usuario = UsuarioDao().eliminar(usuario2)
    log.debug(f'Usuario eliminado: {borrar_usuario}')
    
    
    #listar usuario
    usuarios = UsuarioDao.seleccionar()
    for u in usuarios:
        log.debug(u)
    
    