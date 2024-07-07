class Musica:
    musicas=[]
    
    def __init__(self, nome, duracao, genero, artista):
        self.nome= nome
        self.duracao= duracao
        self.genero= genero
        self.artista= artista
    
    #post
    def create(self):
        Musica.usuarios.append(self)
    
    #get
    def read():
        return Musica.musicas
    
    #put
    def update(self, new_nome,new_genero):
        self.nome= new_nome
        self.genero= new_genero
        
    #delete 
    def delete(self, nome):
        if self.nome== nome:
            musicas.remove(self)
