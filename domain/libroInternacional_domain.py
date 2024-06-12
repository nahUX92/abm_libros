from .libro_domain import Libro

class LibroInternacional(Libro):
    def __init__(self, titulo, autor, isbn, cant_paginas, edicion, editorial, fecha_edicion, pais_origen):
        super().__init__(titulo, autor, isbn, cant_paginas, edicion, editorial, fecha_edicion)
        self.pais_origen = pais_origen