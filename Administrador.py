
import Usuarios as u
import Funciones as f


class Administrador:
    def __init__(self, id, firtsName, email):
        self.id = id
        self.firtsName = firtsName
        self.email = email

    def eliminar_post(self, post):
        post.delete()

    def eliminar_comentario(self, comentario):
        comentario.delete()

    def eliminar_usuario(self, usuario):
        usuario.delete()