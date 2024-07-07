class Album:
    albuns=[]
    
    def __init__(self, nome, duracao, produtora, genero, artista):
        self.nome= nome
        self.duracao= duracao
        self.produtora= produtora
        self.genero= genero
        self.artista= artista
        
    #post
    def create(self):
        Album.albuns.append(self)
    
    #get
    def read():
        return Album.albuns
    
    #put
    def update(self, new_nome):
        self.nome= new_nome
     
    #delete 
    def delete(self, nome):
        if self.nome== nome:
            albuns.remove(self)
