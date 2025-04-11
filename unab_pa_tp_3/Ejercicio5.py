class Persona:
    def __init__(self, nombre, apellido):
        self._nombre = nombre
        self._apellido = apellido
    
    def __str__(self):
        return f"{self._nombre}, {self._apellido}"

class Libro:
    def __init__(self, titulo, autor, isbn, paginas, edicion, editorial, ciudad, pais, fecha_edicion):
        self._titulo = titulo
        self._autor = autor
        self._isbn = isbn
        self._paginas = paginas
        self._edicion = edicion
        self._editorial = editorial
        self._ciudad = ciudad
        self._pais = pais
        self._fecha_edicion = fecha_edicion
    
    # Getters
    def get_titulo(self):
        return self._titulo
    
    def get_autor(self):
        return self._autor
    
    def get_isbn(self):
        return self._isbn
    
    def get_paginas(self):
        return self._paginas
    
    def get_edicion(self):
        return self._edicion
    
    def get_editorial(self):
        return self._editorial
    
    def get_ciudad(self):
        return self._ciudad
    
    def get_pais(self):
        return self._pais
    
    def get_fecha_edicion(self):
        return self._fecha_edicion
    
    # Setters
    def set_titulo(self, titulo):
        self._titulo = titulo
    
    def set_autor(self, autor):
        self._autor = autor
    
    def set_isbn(self, isbn):
        self._isbn = isbn
    
    def set_paginas(self, paginas):
        self._paginas = paginas
    
    def set_edicion(self, edicion):
        self._edicion = edicion
    
    def set_editorial(self, editorial):
        self._editorial = editorial
    
    def set_ciudad(self, ciudad):
        self._ciudad = ciudad
    
    def set_pais(self, pais):
        self._pais = pais
    
    def set_fecha_edicion(self, fecha_edicion):
        self._fecha_edicion = fecha_edicion
    
    # Método para leer información
    def leer_informacion(self):
        return f"Título: {self._titulo}\n" \
               f"Autor: {self._autor}\n" \
               f"ISBN: {self._isbn}\n" \
               f"Editorial: {self._editorial}, {self._ciudad} ({self._pais})\n" \
               f"Fecha de edición: {self._fecha_edicion}\n" \
               f"{self._paginas} páginas"
    
    # Método para mostrar información
    def mostrar_informacion(self):
        print(self.leer_informacion())

# Ejemplo de uso:
autor = Persona("Franz", "Kafka")
libro = Libro(
    titulo="La Metamorfosis",
    autor=autor,
    isbn="0-13-031997-X",
    paginas=784,
    edicion="3a",
    editorial="Ediciones Colihue",
    ciudad="New Jersey",
    pais="USA",
    fecha_edicion="viernes 16 de noviembre de 2001"
)

# Mostrar información
libro.mostrar_informacion()
