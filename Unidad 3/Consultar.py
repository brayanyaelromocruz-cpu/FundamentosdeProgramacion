class Consultar:
    def consultar_libros(self):
        libros = []
        try:
            with open("libros.txt", "r", encoding="utf-8") as f:
                for linea in f:
                    linea = linea.strip()
                    if linea:  # Evita líneas vacías
                        libros.append(linea)
        except FileNotFoundError:
            pass  # Si no existe el archivo, devolvemos la lista vacía
        return libros
