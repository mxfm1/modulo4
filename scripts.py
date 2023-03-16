import json
from individual2 import Alumno, Tesoreria

tes =Tesoreria

def guardar_alumnos():
    with open('alumnos.json','w') as archivo:
        archivo.write(json.dumps(tes.lista_alumnos,default=lambda o: o.__dict__, indent=4))

def recuperar_alunos():
    try:
        with open('alumnos.json') as archivo:
            tes.lista_alumnos = json.loads(archivo.read(), object_hook=lambda d: Alumno(**d))
    except:
        tes.lista_alumnos = []