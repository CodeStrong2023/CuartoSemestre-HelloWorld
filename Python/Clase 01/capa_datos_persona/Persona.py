from logger_base import log

class Persona:
    def __init__(self, id_persona=None, nombre=None, apellido=None, email=None):
        self._id_persona = id_persona
        self._nombre = nombre
        self._apellido = apellido
        self._email = email
        
    def __str__(self):
        return f'''
            Id persona: {self._id_persona},
            Nombre: {self._nombre},
            Apellido: {self._apellido},
            Email: {self._email}
            
            '''
            
    #Metodos Getters and Setters
    @property
    def id_persona(self):
        return self._id_persona
    @id_persona.setter
    def id_persona(self,id_persona):
        self.id_persona
    
    @property
    def nombre(self):
        return self._nombre
    @nombre.setter
    def nombre(self,nombre):
        self._nombre
        
    @property
    def apellido(self):
        return self._apellido
    @apellido.setter
    def apellido(self, apellido):
        self._apellido
    
    @property
    def email(self):
        return self._email
    @email.setter
    def email(self, email):
        self._email

if __name__ == '__main__':
    Persona1=Persona(1,'juan', 'perez', 'jperez@gmail.com')
    log.debug(Persona1)
    Persona2 = Persona(nombre='Jose',apellido='Pereyra',email='jpereyra@email.com')
    log.debug(Persona2)
    Persona1 = Persona(id_persona =1)
    log.debug(Persona1)