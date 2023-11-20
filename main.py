
import requests
import json
import Funciones as f
import Usuarios as u
import Interacciones as i
import Moderacion as m
import Administrador as a
import Multimedia as mu

def main():

    intro = (input (''' 
    -----------------------------------
           ¡ Bienvenido a Metrogram !
    ===== ===== ===== ===== ===== =====
        1 - Registrar usuario
        2 - Buscar perfiles
        3 - Cambiar informacion
        4 - Eliminar datos
        5 - Ver informaciones de usuarios
        6 - Ver todos los usuarios
        7 - (Soy administrador)
        8 - Salir
    ===== ===== ===== ===== ===== =====
    >>>> '''))

    if intro =="1":
        users=f.registrar_nuevo_user(users)
        print(users)
        multimedias= f.menuPost(multimedias)
    elif intro =="2":
        users= f.buscar_perfiless(users)  
    elif intro =="3":
        u.User.change_info
    elif intro == '4':
        u.User.delete_info
    elif intro == '5':
        u.User.show_info
    elif intro == '6':
        f.get_users
    elif intro == '7':
        a.Administrador.eliminar_comentario
        a.Administrador.eliminar_post
        a.Administrador.eliminar_post
    else:
        f.loadBase()
        f.saveBase()
        #Aqui va el pickle
        pass

            
main()