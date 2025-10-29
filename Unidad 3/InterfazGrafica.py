def accion_agregar_libro(self):
    titulo = self.titulo.text()
    autor = self.autor.text()
    mensaje = self.guardar.guardar_libro(titulo, autor)
    self.resultado.setText(mensaje)

def accion_consultar_libros(self):
    libros = self.guardar.consultar_libros()
    if libros:
        texto = "\n".join([f"{libro['titulo']} - {libro['autor']}" for libro in libros])
    else:
        texto = "No hay libros registrados."
    self.resultado.setText(texto)
