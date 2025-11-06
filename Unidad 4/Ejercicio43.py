# -*- coding: utf-8 -*-
"""
Aplicación PyQt5 para registrar alumnos en un archivo de texto.
Ahora incluye un campo de Edad y verifica si el alumno es mayor de edad.
"""

import sys
from pathlib import Path
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QMessageBox,
)


class RegistroAlumnos(QWidget):
    """Ventana principal de la aplicación."""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Registro de Alumnos")
        self.resize(350, 220)

        # ------------------ Widgets ------------------
        # Campo para el nombre
        self.nombre_edit = QLineEdit(self)
        self.nombre_edit.setPlaceholderText("Ej.: Ana García")

        # Campo para la carrera
        self.carrera_edit = QLineEdit(self)
        self.carrera_edit.setPlaceholderText("Ej.: Ingeniería Informática")

        # Campo para la edad
        self.edad_edit = QLineEdit(self)
        self.edad_edit.setPlaceholderText("Ej.: 20")
        self.edad_edit.setMaxLength(3)  # Evita que se escriban edades muy largas
        self.edad_edit.setValidator(None)  # Se puede agregar un validador numérico si se desea

        # Botón Guardar
        self.guardar_btn = QPushButton("Guardar", self)
        self.guardar_btn.clicked.connect(self.guardar_alumno)

        # Botón Limpiar
        self.limpiar_btn = QPushButton("Limpiar", self)
        self.limpiar_btn.clicked.connect(self.limpiar_campos)

        # ------------------ Layout -------------------
        form_layout = QVBoxLayout()

        # Fila de nombre
        fila_nombre = QHBoxLayout()
        fila_nombre.addWidget(QLabel("Nombre:", self))
        fila_nombre.addWidget(self.nombre_edit)
        form_layout.addLayout(fila_nombre)

        # Fila de carrera
        fila_carrera = QHBoxLayout()
        fila_carrera.addWidget(QLabel("Carrera:", self))
        fila_carrera.addWidget(self.carrera_edit)
        form_layout.addLayout(fila_carrera)

        # Fila de edad
        fila_edad = QHBoxLayout()
        fila_edad.addWidget(QLabel("Edad:", self))
        fila_edad.addWidget(self.edad_edit)
        form_layout.addLayout(fila_edad)

        # Botones
        botones_layout = QHBoxLayout()
        botones_layout.addStretch()
        botones_layout.addWidget(self.guardar_btn)
        botones_layout.addWidget(self.limpiar_btn)
        form_layout.addLayout(botones_layout)

        self.setLayout(form_layout)

        # Archivo donde se guardarán los datos
        self.ruta_archivo = Path("alumnos.txt")

    # -------------------------------------------------
    def guardar_alumno(self):
        """Guarda los datos del alumno en un archivo."""
        nombre = self.nombre_edit.text().strip()
        carrera = self.carrera_edit.text().strip()
        edad_texto = self.edad_edit.text().strip()

        # Validar que los campos no estén vacíos
        if not nombre or not carrera or not edad_texto:
            QMessageBox.warning(
                self,
                "Campos incompletos",
                "Debes rellenar el nombre, la carrera y la edad.",
            )
            return

        # Verificar que la edad sea un número válido
        try:
            edad = int(edad_texto)
            if edad <= 0:
                raise ValueError
        except ValueError:
            QMessageBox.warning(
                self,
                "Edad inválida",
                "La edad debe ser un número entero positivo.",
            )
            return

        # Crear la línea de texto que se guardará en el archivo
        linea = f"{nombre} – {carrera} – {edad} años\n"

        # Guardar en el archivo
        try:
            with self.ruta_archivo.open("a", encoding="utf-8") as f:
                f.write(linea)
        except OSError as e:
            QMessageBox.critical(
                self,
                "Error de escritura",
                f"No se pudo guardar el registro.\nDetalle: {e}",
            )
            return

        # Mensaje de confirmación
        if edad >= 18:
            mensaje = f"Alumno guardado correctamente.\n{nombre} es mayor de edad."
        else:
            mensaje = f"Alumno guardado correctamente.\n{nombre} es menor de edad."

        QMessageBox.information(
            self,
            "Guardado",
            mensaje,
        )

        # Limpiar campos después de guardar
        self.limpiar_campos()

    # -------------------------------------------------
    def limpiar_campos(self):
        """Limpia todos los campos de entrada."""
        self.nombre_edit.clear()
        self.carrera_edit.clear()
        self.edad_edit.clear()
        self.nombre_edit.setFocus()


# -----------------------------------------------------
# Punto de entrada de la aplicación
# -----------------------------------------------------
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = RegistroAlumnos()
    ventana.show()
    sys.exit(app.exec_())
