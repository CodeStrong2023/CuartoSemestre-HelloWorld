class Usuario:
    def __init__(self, id_usuario=None, username=None, password=None):
        self._id_usuario = id_usuario
        self._username = username
        self._password = password
        
    def __str__(self):
        return f'''
            Id persona: {self._id_usuario},
            Nombre: {self._username},
            Apellido: {self._password},
            '''
    #Metodos Getters and Setters
    @property
    def id_usuario(self):
        return self._id_usuario
    @id_usuario.setter
    def id_usuario(self,id_usuario):
        self.id_usuario = id_usuario
    
    @property
    def username(self):
        return self._username
    @username.setter
    def nombre(self,username):
        self._username = username
    
    @property
    def password(self):
        return self._password
    @password.setter
    def nombre(self,password):
        self.password = password