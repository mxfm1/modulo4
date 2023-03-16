from dataclasses import dataclass
from scripts import guardar_alumnos,recuperar_alumnos

@dataclass
class Persona:
    rut:str
    nombre:str
    apellido:str

@dataclass
class Alumno(Persona):
    curso:str = '1ero'
    promedio_general:float = 6.1
    sede:str ='Campus Valparaiso'
    saldo:int=0
    creditos:int=0
    deuda:bool=False
    lista_asignaturas = []
    
    @classmethod
    def agregar_asignaturas(self):
        asign = input('Ingresa la asignatura: ')
        self.lista_asignaturas.append(asign)
        print(f'La asignatura {asign} fue creada exitosamente. ')

    @classmethod
    def seleccionar_asignaturas(self,ramo,lista):
        for asign in lista:
            if asign == ramo:
                return asign
        else:
            return None

    @classmethod                
    def mostrar_info(self,alumno,sede=None):
        if alumno is not None:
            if sede is None:
                print(f'El nombre del alumno es: {alumno.nombre}')
            else:
                print(f'El nombre del alumno es: {alumno.nombre} y la sede en la que estudia es: {sede}')
        else:
            print('No existe el alumno. ')

    @classmethod
    def crear_alumnos(self):
            op = input('Deseas agregar alumnos? (S/N)').upper()
            while op not in ['S','N']:
                print('Comando no identificado. Porfavor intenta nuevamente')
                op = input('Deseas agregar alumnoss? (S/N)').upper()
            
            print('----------> INSCRIBIR ALUMNO <----------')
            rut = input('Ingresa el rut: ')
            nombre = input('Nombre: ')
            apellido = input('Apellido: ')
            creditos = int(input('Ingresa los creditos del alumno: '))
            new_alumno = Alumno(rut,nombre,apellido,creditos=creditos)
            Tesoreria.lista_alumnos.append(new_alumno)
            print('Alumno creado exitosamente!! ')

    @classmethod
    def seleccionar_alumno(self):
        print('-----> Búsqueda de Alumnos <-------')
        busqueda = input('Ingresa el RUT del alumno: ')
        for alumno in Tesoreria.lista_alumnos:
            if alumno.rut == busqueda:
                return alumno
        else:
            return None
    @classmethod    
    def verificar_creditos(self,alumno):
        if alumno.creditos > 10:
            print(f'El alumno: {alumno.nombre} puede tomar el ramo.' )
        else:
            print(f'El alumno: {alumno.nombre} no tiene los creditos suficientes para tomar el ramo. ')

            


    # def verificar_creditos(self,alumno):
    #     if alumno.creditos > 10:
    #         print(f'El alumno: {alumno.nombre} puede tomar las asignaturas base.')
    #     elif alumno.creditos > 50:
    #         print(f'El alumno: {alumno.nombre} puede tomar asignaturas electivas. ')
    #     else:
    #         print(f'El alumno: {alumno.nombre} no posee los créditos suficientes para tomar la asignatura. ')

    # def verificar_alumno(self,alumno):
    #     if alumno.saldo

    # def mostrar_alumnos(self):
    #     for alumno in Tesoreria.lista_alumnos:
    #         print(alumno)

    # def seleccionar_alumno(self):
        
    #     self.mostrar_alumnos()
    #     condicion = str(input('Ingresa el rut del alumno: '))
        
    #     for alumno in Tesoreria.lista_alumnos:
    #         if alumno.rut == condicion:
    #             return alumno
    #     else:
    #         return None
        
        

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

    
Alumno.crear_alumnos()
Alumno.crear_alumnos()
guardar_alumnos()
val = Alumno.seleccionar_alumno()
Alumno.mostrar_info(val,)
Alumno.mostrar_info(val,'Campus Valparaiso')
Alumno.verificar_creditos(val)
