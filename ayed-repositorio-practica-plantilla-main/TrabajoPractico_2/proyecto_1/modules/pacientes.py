from random import randint, choices
from datetime import datetime

l_nombres = ['Marcos', 'Maria', 'Valeria', 'Facundo', 'Lucia', 'Lucas']
l_apellido = ['Gonzalez', 'Gross', 'Alvarez', 'Sanchez', 'Argain', 'Murillo']
l_lvl_riesgo = [1, 2, 3]

class paciente:
    def __init__(self, fecha_ingreso=None):
        n = len(l_nombres)
        self.__nombre = l_nombres[randint(0, n-1)]
        self.__apellido = l_apellido[randint(0, n-1)]
        self.__riesgo = l_lvl_riesgo[randint(0, len(l_lvl_riesgo)-1)]
        self.__descripcion = (
            'crítico' if self.__riesgo == 1 else
            'moderado' if self.__riesgo == 2 else
            'bajo')
        self.fecha_ingreso = fecha_ingreso if fecha_ingreso else datetime.now()

    def get_nombre(self):
        return self.__nombre

    def get_apellido(self):
        return self.__apellido

    def get_riesgo(self):
        return self.__riesgo

    def get_descripcion_riesgo(self):
        return self.__descripcion
    
    def __str__(self):
        linea = f"{self.__nombre} {self.__apellido} Nivel de riesgo: {self.__riesgo} ({self.__descripcion}) "
        linea += f"Fecha de ingreso: {self.fecha_ingreso}"
        return linea


    # Métodos de comparación para la cola de prioridad
    def __lt__(self, other):
        if self.__riesgo == other.__riesgo:
            return self.fecha_ingreso < other.fecha_ingreso
        return self.__riesgo < other.__riesgo

    def __eq__(self, other):
        return (self.__riesgo == other.__riesgo and
                self.fecha_ingreso == other.fecha_ingreso)
