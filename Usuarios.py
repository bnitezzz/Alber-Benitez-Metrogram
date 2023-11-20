
import requests 
import json

# usuario = OBJECTO USUARIO # USUARIO ALBER

# siguiendo = []
# for follower in usuario.following:
#     for user in users:
#         if follower == user.id:
#             siguiendo.append(users.username)
#             break

class User():
    def __init__(self,id,firstName, lastName, email, username, type, area,posts,following): 
            self.id = id
            self.firstName = firstName
            self.lastName = lastName
            self.email = email
            self.username = username
            self.type = type
            self.area = area
            self.posts = posts
            self.following = following

    def change_info(self, firstName, lastName, email, username, type, area): 
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.username = username
        self.type = type
        self.area = area
    def show_info(self):
        if self.type=="professor":
            area="Departamento"
        else:
            area="Carrera"

        return f'''
        === === === === === === ===
            Nombre: {self.firstName}, 
            Apellido: {self.lastName}, 
            Email: {self.email},
            Username: {self.username},
            type: {self.type}
            {area}: {self.area},
            Siguiendo: {self.following}
            Posts: {self.posts}
        === === === === === === ==='''
#    def seguidos(self, user):
#            if user not in self.following:
#                self.user.append(user)
            

    def delete_info(self):
        self.firstName = ''
        self.lastName = ''
        self.email = ''
        self.username = ''
        self.type = ''
        self.departmento = ''
        self.carrera = ''
        self.following = ''
        self.posts = ''

