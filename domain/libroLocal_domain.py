from .libro_domain import Libro

class LibroLocal(Libro):
    def __init__(self, titulo, autor, isbn, cant_paginas, edicion, editorial, fecha_edicion, cod_afip):
        super().__init__(titulo, autor, isbn, cant_paginas, edicion, editorial, fecha_edicion)
        self.cod_afip = cod_afip