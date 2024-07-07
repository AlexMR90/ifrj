class Usuario:
    usuarios =[]
    
    def __init__(self, nome, login, senha):
        self.nome= nome
        self.login= login
        self.senha= senha
    
    #post
    def create(self):
        Usuario.usuarios.append(self)
    
    #get
    def read():
        return Usuario.usuarios
    
    #put
    def update(self, new_nome,new_login, new_senha):
        self.nome= new_nome
        self.login= new_login
        self.senha= new_senha
     
    #delete 
    def delete(self, login):
        if self.login== login:
            usuarios.remove(self)
