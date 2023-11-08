class Libros:
    def _init_(self, titulo, autor, num_ejemplares):
        self.titulo = titulo
        self.autor = autor
        self.num_ejemplares = num_ejemplares
        self.num_prestados = 0

    def prestamo(self):
        if self.num_prestados < self.num_ejemplares:
            self.num_prestados += 1
            return True
        return False

    def devolucion(self):
        if self.num_prestados > 0:
            self.num_prestados -= 1
            return True
        return False

    def _str_(self):
        return f"Libro: {self.titulo}\nAutor: {self.autor}\nEjemplares disponibles: {self.num_ejemplares - self.num_prestados}\nEjemplares prestados: {self.num_prestados}"

# Ejemplo de uso
libro1 = Libros("La Odisea", "Homero", 5)
libro2 = Libros("Cien años de soledad", "Gabriel García Márquez", 3)

print(libro1)  # Muestra los datos del libro 1
print(libro2)  # Muestra los datos del libro 2

libro1.prestamo()
libro1.prestamo()
libro2.prestamo()
libro1.devolucion()

print(libro1)  # Muestra los datos actualizados del libro 1
print(libro2)  # Muestra los datos actualizados del libro 2