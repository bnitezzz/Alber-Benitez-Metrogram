
import Usuarios as u
import Funciones as f
import Multimedia as m


### Aqui estaran para ver los like de seguidores 
class Interacciones():

    follow = u.User.following 

    def __init__(self, post, follow,):
        self.post = post
        self.follow = follow

    def seguidos(self, user):
            if user not in self.following:
                print('No sigues este usuario')
                self.user.append(user)
            elif self not in user.follower:
                    print('No sigues a este usuario')
                    user.follower.append(self)



