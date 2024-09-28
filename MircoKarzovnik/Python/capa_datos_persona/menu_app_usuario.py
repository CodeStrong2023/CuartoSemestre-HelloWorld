from usuarioDAO import UsuarioDao
from logger_base import log
from usuario import Usuario
opcion = 0
while opcion <= 5:
    print('Opciones: ')
    print('1-Listar usuario')
    print('2-Agregar usuario')
    print('3-Modificar Usuario')
    print('4-Eliminar Usuario')
    print('5-Salir')
    opcion = int(input('Digite la opcion (1-5): '))
    if opcion == 1:
        usuarios = UsuarioDao.seleccionar()
        for u in usuarios:
            log.info(u)
    if opcion == 2:
        username = input('Digite el nombre del usuario: ')
        password = int(input('Digite la contraeña numerica: '))
        usuario_a_agregar= Usuario(username=username,password=password)
        usuarioAgregado = UsuarioDao.insertar(usuario_a_agregar)
        log.info(f'el usuario agregado es: {usuarioAgregado}') 
    if opcion == 3:
        usuario_a_modificar= int(input('Dime el ID del usuario a modificar'))
        username = input('Dime el nuevo username: ')
        password = int(input('Digite la nueva contraseña numerica'))
        usuario_modificado = UsuarioDao.actualizar(Usuario(id_usuario=usuario_a_modificar,username=username,password=password))
        log.info(f'El usuario modificado es: {usuario_modificado}')
    if opcion == 4:
        id_usuario=int(input('Digite el 4id del usuario a borrar: '))
        usuario_a_borrar = Usuario(id_usuario=id_usuario)
        usuario_eliminado = UsuarioDao.eliminar(usuario_a_borrar)
        log.info(f'se borro el usuario: {usuario_eliminado}')
else:
    log.info('Salimos de la apliacion')