from dal.libro_dal import Libro_DAL

class Libro_BLL:
    def __init__(self):
        self.librosDAL = Libro_DAL()

    @staticmethod
    def str_libro(libro):
        return f"Titulo: {libro.titulo} {libro.edicion} edicion, Autor: {libro.autor}, ISBN: {libro.isbn}, {libro.editorial}, fecha {libro.fecha_edicion}, {libro.cant_paginas} páginas"
    
    @staticmethod
    def get_categoria(libro):
        if libro.cant_paginas == 0:
            return "Libro sin establecer"
        elif libro.cant_paginas < 200:
            return "Libro corto"
        elif 200 <= libro.cant_paginas < 500:
            return "Libro convencional"
        else:
            return "Libro extenso"
        
    def insertar_libro(self, libro):
        self.librosDAL.insertar_libro(libro)

    def obtener_libro(self, isbn):
        return self.librosDAL.obtener_libro(isbn)