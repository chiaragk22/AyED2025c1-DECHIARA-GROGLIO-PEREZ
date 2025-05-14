from random import randint, choices

l_nombres = ['Marcos, Maria, Valeria, Facundo, Lucia, Lucas']
l_apellido = ['Gonzalez, Gross, Alvarez, Sanchez, Argain, murillo']
l_lvl_riesgo = [1, 2, 3]

class paciente:
    def _init_(self):
        n = len(l_nombres)
        self.__nombre = l_nombres[randint(0, n-1)]
        self.__apellido = l_apellido[randint(0, n-1)]
        self.__riesgo = l_lvl_riesgo[randint(0, len(l_lvl_riesgo)-1)]
        self.__descripcion = (
            'crítico' if self.__riesgo == 1 else
            'moderado' if self.__riesgo == 2 else
            'bajo'
        )
    def get_nombre(self):
        return self.__nombre
    def get_apellido(self):
        return self.__apellido
    def get_riesgo(self):
        return self.__riesgo
    def get_descripcion_riesgo(self):
        return self.__descripcion
    def _str_(self):
        linea = self.__nombre + ' '
        linea += self.__apellido + ' ' + 'Nivel de riesgo: ' '
        linea += str(self._riesgo) + (self._descripcion)
        return linea