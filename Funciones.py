import Multimedia as m
from Usuarios import User
import requests
import json
import pickle
import Interacciones as i



### Aqui estaran todas las funciones que necesitamos para que el programa me corra
### que seran llamadas en el main o para complementar las demas 
### Traduccion de la estructura de la API a la estructura que se va a utilizar
def get_users():
    ### Realizamos una petición get a la API
    r = requests.get('https://raw.githubusercontent.com/Algoritmos-y-Programacion-2223-3/api-proyecto/08d4d2ce028692d71e9f8c32ea8c29ae24efe5b1/users.json')
    users_api = r.json()

    users = []

    for user in users_api:
        parameters = []
        for parameter,value in user.items():
            parameters.append(value)

        new_user = User(parameters[0],parameters[1],parameters[2],parameters[3],parameters[4],parameters[5],parameters[6],[],parameters[7])
        users.append(new_user)
    ### Luego imprimimos todos los usuarios 
    return users
def registrar_nuevo_user(users):
        firstName = input ('Ingresa nombre: ')
        lastName = input ('Ingrese Apellido: ')
        email = input ('Ingrese correo electronico: ')
        while "@" not in email:
            email = input ('''
               << ERORR >>
            ==== Ingrese correo electronico: ''')
        username = input ('Ingrese su nombre de usuario: ')
        while " " in username:
            username = input ('''
               << Error, no puede tener espacio !VERIFIQUELO¡ >>
            ==== Ingrese su nombre de usuario: ''')
        type = input('''' 
            ==== ==== ==== ==== ====
            Estudia alguna carrera:
            1 - Si
            2 - No
        >>> ''')
        if type == '1':
            area = input (f'''
            Bienvenido Estudiante {username}
            ¿cual es su carrera? : ''')
        else:
            area = input (f'''
            Bienvenido Profesor {firstName}
            ¿Cual es su departamento?: ''')

        new_user = User(len(users) + 1,firstName, lastName, email, username, type, area, [],[])

        print(new_user)

        users.append(new_user)


        return users
def menuPost():
    while True:
        ver = input('''
        -----------------------------------
            ¡ Post !
        ===== ===== ===== ===== ===== =====
            1 - Resgistrar Post
            2 - Ver Post de following
            3 - Buscar Post (filtro Usuario)
            4 - Buscar Post (filtro Hashtags) 
            -
            5 - Salir 
        ===== ===== ===== ===== ===== =====
        ''')
        if ver == '1':
            m.Multimedia.registrarPost()
        elif ver == '2':
            m.Multimedia.getPost()
        elif ver == '3':
            m.Multimedia.buscarPostUser()
        elif ver == '4':
            m.Multimedia.buscarPostHashtag()
        else:
            print('''   
        -----------------------------------
            ¡ Nos vemos, regresa pronto !
        ===== ===== ===== ===== ===== =====''')
    else:
        pass
def guardar_users(self, users):
    with open("users.json", "w") as file:
        json.dump(users, file)
def buscar_perfiless(self, filter_by, value):
    users = self.users()
    filtro_users = []   
    for user in users:
        if filter_by == "username" and user["username"] == value:
                    filtro_users.append(user)
        elif filter_by == "departmento" and user["departmento"] == value:
                    filtro_users.append(user)
        return filtro_users
    return menuPost
### Pickle: Función recibe dos parámetros: el objeto con los datos a serializar, y el archivo donde se van a escribir
def saveBase(database):
    with open("database.pkl", "wb") as file:
        pickle.dump(database, file) 
def loadBase():
    with open("database.pkl", "rb") as file:
        return pickle.load(file)
def infoEstudiante(users):
    for user in users:
        if user.type == "student":
                print(user.show_info())
    else:
            pass
def infoProfesores(users):
    for user in users:
        if user.type == "professor":
                print(user.show_info())
    else:
            pass
def menuFollow():
    ver = ('''
        -----------------------------------
            ¡ Following !
        ===== ===== ===== ===== ===== =====
            1 - Ver seguidores
            2 - Ver post de seguidos 
            - 
            3 - Salir 
        ===== ===== ===== ===== ===== =====
        ''')
    if ver == '1':
        i.Interacciones.follow
    elif ver == '2':
        pass
    else: 
        print('''   
        -----------------------------------
            ¡ Nos vemos, regresa pronto !
        ===== ===== ===== ===== ===== =====''')