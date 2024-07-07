class Artista:
    artistas=[]
    
    def __init__(self, nome, biografia, generoPrincipal):
        self.nome= nome
        self.biografia= biografia
        self.generoPrincipal= generoPrincipal
    
    #post
    def create(self):
        Artista.artistas.append(self)
    
    #get
    def read():
        return Artista.artistas
    
    #put
    def update(self, new_nome, new_biografia, new_generoPrincipal):
        self.nome= new_nome
        self.biografia= new_biografia
        self.generoPrincipal= new_generoPrincipal
    
    #delete
    def delete(self, nome):
        if self.nome== nome:
            artistas.remove(self)