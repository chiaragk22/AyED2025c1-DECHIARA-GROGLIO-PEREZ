import math

class Cilindro:
    def __init__(self, radio, altura):
        if radio <= 0 or altura <= 0:
            raise ValueError("Radio y altura deben ser positivos")
        self.radio = radio
        self.altura = altura
    
    def volumen(self):
        return math.pi * (self.radio ** 2) * self.altura
    
    def area_superficial(self):
        return 2 * math.pi * self.radio * (self.radio + self.altura)