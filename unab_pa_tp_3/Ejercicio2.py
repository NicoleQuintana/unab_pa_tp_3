class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def eje_x(self):
        return self.x
    
    def eje_y(self):
        return self.y
    
    def impresion(self):
        return f"({self.x}, {self.y})"
    
    def opuesto(self):
        return Punto(-self.x, -self.y)
    
    def distancia_origen(self):
        return (self.x**2 + self.y**2)**0.5
    
    def __str__(self):
        return self.impresion()


# Crear un punto
p1 = Punto(3, 4)

# Mostrar coordenadas
print("Coordenada x:", p1.eje_x())  # Imprime: 3
print("Coordenada y:", p1.eje_y())  # Imprime: 4

# Imprimir punto
print("Representación del punto:", p1.impresion())  # Imprime: (3, 4)

# Crear punto opuesto
p2 = p1.opuesto()
print("Punto opuesto:", p2.impresion())  # Imprime: (-3, -4)

# Calcular distancia al origen
print("Distancia al origen:", p1.distancia_origen())  # Imprime: 5.0
