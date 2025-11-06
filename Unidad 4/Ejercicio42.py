# -*- coding: utf-8 -*-
"""
Aplicación sencilla en PyQt5 para enviar pings a un host o dirección IP.

Requisitos:
- Tener instalado PyQt5
- Conexión a internet (para probar con hosts externos)
"""

# -----------------------------
# Librerías importadas y su función
# -----------------------------

import sys              # Permite acceder a los argumentos del sistema y salir de la app correctamente.
import platform         # Sirve para detectar el sistema operativo (Windows, Linux, etc.).
import subprocess        # Permite ejecutar comandos del sistema (como "ping") desde Python.

# Librerías de PyQt5 para la interfaz gráfica
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication,   # Inicializa la aplicación
    QWidget,        # Clase base para la ventana principal
    QLabel,         # Muestra texto estático
    QLineEdit,      # Campo de texto de una línea (entrada del host)
    QPushButton,    # Botón para ejecutar la acción de ping
    QTextEdit,      # Área de texto para mostrar resultados
    QVBoxLayout,    # Layout vertical (organiza elementos uno debajo del otro)
    QHBoxLayout,    # Layout horizontal (organiza elementos en línea)
    QMessageBox,    # Ventana emergente para mostrar mensajes
)


# -----------------------------
# Clase principal de la aplicación
# -----------------------------
class PingApp(QWidget):
    """Ventana principal de la aplicación Ping."""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ping – PyQt5")
        self.resize(400, 300)

        # ---------- Widgets ----------
        # Campo de texto donde el usuario introduce la IP o el dominio
        self.host_input = QLineEdit(self)
        self.host_input.setPlaceholderText("Ejemplo: google.com o 8.8.8.8")

        # Botón para ejecutar el ping
        self.ping_btn = QPushButton("Enviar ping", self)
        self.ping_btn.clicked.connect(self.ejecutar_ping)  # Conecta el clic con la función

        # Cuadro de texto donde se mostrará el resultado del comando ping
        self.resultado = QTextEdit(self)
        self.resultado.setReadOnly(True)  # El usuario no puede editar el resultado

        # ---------- Layout ----------
        # Fila con etiqueta "Destino" y el campo de entrada
        entrada_layout = QHBoxLayout()
        entrada_layout.addWidget(QLabel("Destino:", self))
        entrada_layout.addWidget(self.host_input)

        # Layout principal (vertical)
        main_layout = QVBoxLayout()
        main_layout.addLayout(entrada_layout)
        main_layout.addWidget(self.ping_btn)
        main_layout.addWidget(QLabel("Resultado:", self))
        main_layout.addWidget(self.resultado)

        # Aplica el layout a la ventana principal
        self.setLayout(main_layout)

    # -----------------------------------------------------------------
    def ejecutar_ping(self):
        """Ejecuta el comando 'ping' y muestra el resultado en pantalla."""
        host = self.host_input.text().strip()  # Elimina espacios en blanco
        if not host:
            # Si el campo está vacío, muestra una advertencia
            QMessageBox.warning(self, "Entrada vacía", "Introduce una dirección IP o nombre de host.")
            return

        # Detectar sistema operativo para usar el parámetro correcto
        sistema = platform.system().lower()
        if "windows" in sistema:
            cmd = ["ping", "-n", "4", host]   # -n = número de pings en Windows
        else:
            cmd = ["ping", "-c", "4", host]   # -c = número de pings en Linux/macOS

        try:
            # Ejecutar el comando y capturar la salida (stdout y stderr)
            proceso = subprocess.run(
                cmd,
                capture_output=True,  # Captura la salida del comando
                text=True,            # Devuelve texto (no bytes)
                timeout=10,           # Máximo 10 segundos de espera
            )

            # Mostrar salida dependiendo del resultado
            if proceso.returncode == 0:
                salida = proceso.stdout  # Éxito → mostrar salida estándar
            else:
                salida = proceso.stderr  # Error → mostrar salida de error

            self.resultado.setPlainText(salida)

        except subprocess.TimeoutExpired:
            self.resultado.setPlainText("Error: tiempo de espera agotado.")
        except Exception as e:
            self.resultado.setPlainText(f"Ocurrió un error inesperado:\n{e}")


# -----------------------------
# Punto de entrada del programa
# -----------------------------
if __name__ == "__main__":
    app = QApplication(sys.argv)  # Crea la aplicación Qt
    ventana = PingApp()           # Crea la ventana principal
    ventana.show()                # Muestra la ventana
    sys.exit(app.exec_())         # Inicia el bucle principal de eventos
