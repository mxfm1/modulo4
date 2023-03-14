from dataclasses import dataclass

class Persona:

    def __init__(self,rut,nombre,apellido):
        self.rut:str = rut
        self.nombre:str = nombre
        self.apellido:str = apellido

@dataclass
class Alumno(Persona):
    curso:str
    promedio_general:float
    sede:str
    saldo:int
    creditos:int
    deuda:bool=False

    def mostrar_info(self,curso,sede):
        print(f'El alumno: {self.nombre} se encuentra cursando el {curso} en la sede: {sede}')

    def mostrar_info(self,creditos,saldo,x):
        print(f'Los datos del alumno: {self.nombre} son: creditos -> {creditos} saldo-> {saldo} y el ultimo dato es: {x}')

    def agregar_alumno():
        if len(Tesoreria.lista_alumnos) == 0:
            op = input('Deseas agregar alumnos? (S/N)').upper()
            while op not in ['S','N']:
                print('Comando no identificado. Porfavor intenta nuevamente')
                op = input('Deseas agregar alumnoss? (S/N)').upper()
    def agregar_curso():
        pass


@dataclass
class Profesor(Persona):
    materia:str
    sede:str
    horas_semanales:float
    sueldo:int

@dataclass
class jefeCarrera(Persona):
    materia:str
    sede:str
    sueldo:int
    horas_semanales:float

@dataclass
class Tesoreria:
    lista_asignaturas=[]
    lista_alumnos=[]
    lista_profesores = []
    recaudacion:float
    distribucion_horas = int

    
a1 = Alumno()