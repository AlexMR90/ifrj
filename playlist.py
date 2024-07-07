class Playlist:
    playlists=[]
    def __init__(self, nome, duracao):
        self.nome= nome
        self.duracao= duracao
    
        #post
    def create(self):
        Playlist.playlists.append(self)
    
    #get
    def read():
        return Playlist.playlists
    
    #put
    def update(self, new_nome):
        self.nome= new_nome
     
    #delete 
    def delete(self, nome):
        if self.nome== nome:
            playlists.remove(self)
            