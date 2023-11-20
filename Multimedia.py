
import datetime
class Multimedia():                                 
    def __init__(self, user_id, media, descripcion, hashtags, date, likes, comentarios):
        self.user_id = user_id
        self.media = media ###------->>> foto o video
        self.descripcion = descripcion
        self.hashtags = hashtags
        self.date = date 
        self.likes = likes  ###------>>> Nro int de likes  
        self.comentarios = comentarios ###-------->>> Lista que contiene comentarios (strings)
    def darLike(self):
        self.like+=1
    def escribirComentario(self):
        comentario = input("Ingresa tu comentario")
        self.comentarios.append(comentario)    
    def getPost(self):
            return {
            "user": self.user_id,"media": self.media,"description": self.descripcion,"hashtags": self.hashtags,"date": self.date
                }

    def buscarPostUser(self, user):
        return [post for post in self.posts if post.user == user]
    
    def buscarPostHashtag(self, hashtag):
        return [post for post in self.posts if hashtag in post.hashtag]
    
   
    def delete_post(self):
        self.user_id = ''
        self.media = ''
        self.descripcion = ''
        self.hashtags = ''
        self.date = ''
        self.likes = ''
        self.comentarios =''
            
    def registrarPost(self, multimedia):
        user_id = input('Ingrese su User id: ')
        media = input('Cargue su archivo media aqui: ')
        descripcion = input('Ingrese la descripcion del post: ')
        hashtags = input ('Agregue los hashtags favoritos tuyos: ')
        date = datetime.now

        new_post = Multimedia(user_id,media, descripcion,hashtags,date)
        return new_post


        



                    
