class Cancion:
    def __init__(self, titulo, autor):
        self._titulo = titulo
        self._autor = autor
    
    def get_titulo(self):
        return self._titulo
    
    def get_autor(self):
        return self._autor
    
    def set_titulo(self, titulo):
        self._titulo = titulo
    
    def set_autor(self, autor):
        self._autor = autor

# Ejemplo de uso:
# Crear una canción
mi_cancion = Cancion("Creep", "Radiohead")

# Obtener título y autor
print(mi_cancion.get_titulo())  # Imprime: Creep
print(mi_cancion.get_autor())   # Imprime: Radiohead

# Cambiar título y autor
mi_cancion.set_titulo("All Apologies")
mi_cancion.set_autor("Nirvana")

# Verificar los nuevos valores
print(mi_cancion.get_titulo())  # Imprime: All Apologies
print(mi_cancion.get_autor())   # Imprime: Nirvana
