# -*- coding: utf-8 -*-

class Alumno:
    def __init__(self, nombre: str, numero_control: str, carrera=None, curp: str = None):
        self.nombre = nombre                # Nombre del alumno (tipo: str / VARCHAR)
        self.numero_control = numero_control  # Número de control del alumno (tipo: str / VARCHAR)
        self.carrera = carrera              # Carrera que escogió el alumno (tipo: objeto Carrera / FK)
        self.calificaciones = {}            # Calificaciones del alumno (tipo: dict {materia: float})
        self.curp = curp                    # CURP del alumno (tipo: str / CHAR(18))

    def asignar_carrera(self, carrera):
        self.carrera = carrera

    def consulta_calificacion(self, nombre_materia: str):
        if nombre_materia in self.calificaciones:
            return self.calificaciones[nombre_materia]
        else:
            return f'No hay calificación registrada para "{nombre_materia}".'

    def __repr__(self):
        return f'Alumno("{self.nombre}", "{self.numero_control}")'


class Universidad:
    def __init__(self, nombre: str, id_profesor: int = None):
        self.nombre = nombre                # Nombre de la universidad (tipo: str / VARCHAR)
        self.carreras = []                  # Lista de carreras (tipo: list[Carrera])
        self.alumnos = []                   # Lista de alumnos (tipo: list[Alumno])
        self.profesores = []                # Lista de profesores (tipo: list[Profesor])
        self.id_profesor = id_profesor      # Identificador del profesor (tipo: int / PRIMARY KEY)

    # ------------------- Gestión de carreras -------------------
    def agregar_carrera(self, carrera):
        self.carreras.append(carrera)

    def obtener_carrera(self, nombre_carrera: str):
        for c in self.carreras:
            if c.nombre == nombre_carrera:
                return c
        return None

    # ------------------- Otros registros -------------------
    def agregar_alumno(self, alumno):
        self.alumnos.append(alumno)

    def agregar_profesor(self, profesor):
        self.profesores.append(profesor)


class Carrera:
    def __init__(self, nombre: str, profesores=None):
        self.nombre = nombre                # Nombre de la carrera (tipo: str / VARCHAR)
        self.materias = []                  # Lista de materias asociadas (tipo: list[Materia])
        self.profesores = profesores or []  # Lista de profesores (tipo: list[Profesor])

    def agregar_materia(self, materia):
        self.materias.append(materia)

    def obtener_materia(self, nombre_materia: str):
        for m in self.materias:
            if m.nombre == nombre_materia:
                return m
        return None

    def __repr__(self):
        return f'Carrera("{self.nombre}")'


class Materia:
    def __init__(self, nombre: str, carrera: Carrera, calificacion_final: float = None, semestre: int = 1):
        self.nombre = nombre                # Nombre de la materia (tipo: str / VARCHAR)
        self.carrera = carrera              # Instancia de la carrera (tipo: objeto Carrera / FK)
        self.calificacion_final = calificacion_final  # Calificación final (tipo: float / DECIMAL(3,1))
        self.semestre = semestre            # Semestre en el que se cursa (tipo: int)

    def __repr__(self):
        return f'Materia("{self.nombre}", carrera="{self.carrera.nombre}")'


class Profesor:
    def __init__(self, nombre: str, materia: Materia, horario: str = None):
        self.nombre = nombre                # Nombre del profesor (tipo: str / VARCHAR)
        self.materia = materia              # Materia que imparte (tipo: objeto Materia / FK)
        self.horario = horario              # Horario del profesor (tipo: str / VARCHAR)

    def registra_calificacion(self, alumno: Alumno, calificacion: float):
        alumno.calificaciones[self.materia.nombre] = calificacion
        print(f'Calificación registrada: {alumno.nombre} -> '
              f'{self.materia.nombre}: {calificacion}')

    def __repr__(self):
        return f'Profesor("{self.nombre}", {self.materia})'


if __name__ == "__main__":

    uni = Universidad("Instituto")

    ing = Carrera("Ingeniería")
    lic = Carrera("Licenciatura en Ciencias Sociales")

    uni.agregar_carrera(ing)
    uni.agregar_carrera(lic)

    calc = Materia("Cálculo I", ing)
    fis = Materia("Física I", ing)
    sociologia = Materia("Introducción a la Sociología", lic)

    ing.agregar_materia(calc)
    ing.agregar_materia(fis)
    lic.agregar_materia(sociologia)

    juan = Alumno("Juan Pérez", "2023001", curp="PEJJ800101HDFRNN01")
    luisa = Alumno("Luisa Gómez", "2023002", curp="GOML900202MDFLRS02")

    juan.asignar_carrera(ing)
    luisa.asignar_carrera(ing)

    uni.agregar_alumno(juan)
    uni.agregar_alumno(luisa)

    prof_garcia = Profesor("Dr. García", calc, horario="Lunes a Viernes 9-11 AM")
    prof_rodriguez = Profesor("Mtra. Rodríguez", fis, horario="Lunes a Viernes 11-1 PM")

    uni.agregar_profesor(prof_garcia)
    uni.agregar_profesor(prof_rodriguez)

    prof_garcia.registra_calificacion(juan, 8.5)
    prof_garcia.registra_calificacion(luisa, 9.0)
    prof_rodriguez.registra_calificacion(juan, 7.5)

    print(juan.consulta_calificacion("Cálculo I"))
    print(juan.consulta_calificacion("Física I"))
    print(luisa.consulta_calificacion("Cálculo I"))
    print(luisa.consulta_calificacion("Física I"))

    print("Materias de Ingeniería:", [m.nombre for m in ing.materias])
