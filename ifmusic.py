from fastapi import FastAPI
from pydantic import BaseModel
from album import Album
from artista import Artista
from musica import Musica
from playlist import Playlist
from usuario import Usuario

api= FastAPI()

class album_model(BaseModel):
    nome:str    
class artista_model(BaseModel):
    nome:str
class musica_model(BaseModel):
    nome:str
class playslist(BaseModel):
    nome:str
class usuario(BaseModel):
    nome:str

@api.post("/albuns")
def create_album():
    album_novo = Album()
    Album.create()

@api.get("/albuns")
def read_album():
    return Album.read()


@api.post("/artistas")
def create_artista():
    artista_novo = Artista()
    Artista.create()

@api.get("/artistas")
def read_artista():
    return Artista.read()

@api.post("/musicas")
def create_musica():
    musica_novo = Musica()
    Musica.create()

@api.get("/musicas")
def read_musica():
    return Musica.read()

@api.post("/playlists")
def create_playlist():
    playlist_novo = Playlist()
    playslist.create()

@api.get("/playlists")
def read_playlist():
    return Playlist.read()

@api.post("/usuarios")
def create_usuario():
    usuario_novo = usuario()
    Usuario.create()

@api.get("/usuarios")
def read_usuario():
    return Usuario.read()