class Guardar:
    def guardar_libro(self, titulo, autor):
        if not titulo or not autor:
            return "Error: Debes ingresar tanto el título como el autor."

        try:
            with open("libros.txt", "a", encoding="utf-8") as f:
                f.write(f"{titulo} - {autor}\n")
            return f"Libro '{titulo}' guardado correctamente."
        except Exception as e:
            return f"Error al guardar el libro: {e}"
