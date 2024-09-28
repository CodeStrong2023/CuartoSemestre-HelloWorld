from conexion import Conexion
from Persona import Persona
from logger_base import log
from cursor_del_pool import CursorDelPool

class PersonaDao:
    
    ''' 
    DAO significa: Data Access Object
    CRUD significa:
        creaate -> insertar
        read -> seleccionar
        update -> actualizar
        delte -> eliminar
    '''
    _SELECCIONAR = 'SELECT * FROM persona ORDER BY id_persona'
    _INSERTAR = 'INSERT INTO persona(nombre, apellido, email) VALUES (%s,%s,%s)'
    _ACTUALIZAR = 'UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s'
    _ELIMINAR = 'DELETE FROM persona WHERE id_persona=%s'
        
    #definimos los metodos de la clase
    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            personas=[]
            for registro in registros:
                persona = Persona(registro[0],registro[1],registro[2],registro[3])
                personas.append(persona)
            return personas
    @classmethod
    def insertar(cls, persona):
       
        with CursorDelPool() as cursor:
            valores = (persona.nombre,persona.apellido, persona.email)
            cursor.execute(cls._INSERTAR,valores)
            log.debug(f'Persona insertada: {persona}')
            return cursor.rowcount 
    @classmethod
    def actualizar(cls, persona):  
        with CursorDelPool() as cursor:
            valores = (persona.nombre,persona.apellido, persona.email,persona.id_persona)
            cursor.execute(cls._ACTUALIZAR,valores)
            log.debug(f'Persona actualizada: {persona}')
            return cursor.rowcount 
    @classmethod
    def eliminar(cls, persona):
        with CursorDelPool() as cursor:
            valores=(persona.id_persona,)
            cursor.execute(cls._ELIMINAR,valores)
            log.debug('los objetos eliminados son: {persona}')
            return cursor.rowcount
                    
    
            
        
                    
if __name__ == '__main__':
    """ #Eliminar un objeto
    persona1 = Persona(id_persona=1)
    personas_eliminadas= PersonaDao.eliminar(persona1)
    log.debug(f'personas eliminadas: {personas_eliminadas}')
    #Actualizar objeto
    persona2 = Persona(11,'Chompira','Morales','chompirito@email.com')
    personasActualizadas = PersonaDao.actualizar(persona2) """
    #Insertar objeto
    persona1 = Persona(nombre='Leandro',apellido='Eugenio',email='leugenio@email.com')
    personasInsertadas = PersonaDao.insertar(persona1)
    log.debug(f'personas insertadas: {personasInsertadas}')
    
    """ #Seleccionar Objeto
    personas = PersonaDao.seleccionar()
    for p in personas:
        log.debug(p)                      """