from domain.autor_domain import Autor
from domain.editorial_domain import Editorial
from domain.libroLocal_domain import LibroLocal
from domain.libroInternacional_domain import LibroInternacional
from bll.Libro_bll import Libro_BLL

# Instancias de las clases
autor_1=Autor("Jones", "Beyer")
editorial_1=Editorial("O'Reilly", "Sebastopol, CA", "USA")
libro_local=LibroLocal("Site Reliability Engineering", autor_1, "978-1-491-92912-4", 524, "4", editorial_1, "2018-10-19", "AFIP123")
libro_internacional=LibroInternacional("Site Reliability Engineering", autor_1, "978-1-491-92912-4", 524, "4", editorial_1, "2018-10-19", "USA")

# Instancia de la BLL de libro
logica_libro=Libro_BLL()

# Insertar libros usando su bll
logica_libro.insertar_libro(libro_local)
logica_libro.insertar_libro(libro_internacional)

# Buscams un libro por su ISBN y lo devolvemos
libro_obtenido = logica_libro.obtener_libro("978-1-491-92912-4")
print(Libro_BLL.str_libro(libro_obtenido))

# Buscamos que categorai es el libro y imprimos.
categoria_libro=Libro_BLL.get_categoria(libro_obtenido)
print(f"El libro \"{libro_obtenido.titulo}\", con ISBN: {libro_obtenido.isbn} es un libro bajo la categoria: {categoria_libro}.")