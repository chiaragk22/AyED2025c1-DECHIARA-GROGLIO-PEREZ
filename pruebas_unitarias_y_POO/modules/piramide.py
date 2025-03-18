import math

class Piramide:
    # *** Constructor: Debe validar que base_longitud y altura sean positivos, luego asignarlos a los atributos
    def __init__(self, base_longitud, altura):
        # Escriban su código acá)
        pass
    
    # *** Método volumen: Debe calcular (base_longitud² * altura) / 3
    def volumen(self):
        # Escriban su código acá)
        pass
    
    # *** Método area_superficial: Fórmula area = base_longitud * (base_longitud + math.sqrt(4*altura² + (base_longitud/2)²))
    def area_superficial(self):
        # Escriban su código acá)
        pass


















































# class Piramide:
#     def __init__(self, base_longitud, altura):
#         if base_longitud <= 0 or altura <= 0:
#             raise ValueError("base_longitud y altura deben ser positivos")
#         self.base_longitud = base_longitud
#         self.altura = altura
    
#     def volumen(self):
#         return (self.base_longitud ** 2 * self.altura) / 3
    
#     def area_superficial(self):
#         area = self.base_longitud * (self.base_longitud + math.sqrt(4*self.altura**2 + (self.base_longitud/2)**2))
#         return area