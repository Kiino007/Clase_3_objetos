class Rectangulo:
    def __init__(self, ancho, alto):
        self._ancho = ancho
        self._alto = alto

    @property
    def area(self): #propiedad que va calcular el area del rectangulo sin exponer la formula
        return self.ancho * self._alto

    @property
    def perimetro(self): #calcular perimetro del rectangulo
        return 2 * (self._ancho + self._alto)

    def escalar(self, factor): #metodo publico para cambiar el tamaño sin exponer como se modifican los atributos
        if factor <= 0:
            raise ValueError("El factor debe ser mayor que cero")
        self._ancho *= factor
        self._alto *= factor 

r = Rectangulo(4, 3)
print("area:", r.area)
print("Perimetro", r.perimetro)

r.escalar(2)
print("Area tras escalar: ", r.area)

