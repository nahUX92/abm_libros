from domain.libro_domain import Libro

class Libro_DAL:
    def __init__(self):
        self.libros = {}

    def insertar_libro(self,libro):
        self.libros[libro.isbn] = libro

    def obtener_libro(self,isbn):
        return self.libros.get(isbn, None)