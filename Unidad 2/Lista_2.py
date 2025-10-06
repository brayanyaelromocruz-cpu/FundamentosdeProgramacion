for i in range(1, 5):
    print("Número", i)

print()

suma = 0
for i in range(1, 11):
    suma += i
print("La suma de los primeros 10 números es:", suma)

print()

nombres = ["Ed", "Jorge", "María", "Luisa"]
for nombre in nombres:
    print("Hola,", nombre)

print()

Cumple = int(input("¿Cuál es tu edad? "))
for i in range(1, Cumple):
    print("Feliz cumpleaños número", i)

print()

opcion = int(input("Elige una opción (1 = guardar, 2 = abrir, 3 = salir): "))
if opcion == 1:
    print("Has elegido guardar el archivo")
elif opcion == 2:
    print("Has elegido abrir un archivo")
elif opcion == 3:
    print("Has elegido salir del programa")
else:
    print("Opción no válida")

print()

calificacion = int(input("Ingresa tu calificación: "))
if calificacion >= 90:
    print("Excelente")
elif calificacion >= 70:
    print("Aprobado")
else:
    print("Reprobado")

print()

numero_secreto = 7
adivinanza = 0
while adivinan za != numero_secreto:
    adivinanza = int(input("Adivina el número (1-10): "))
print("¡Correcto! El número era", numero_secreto)

print()

contador = 1
while contador <= 5:
    print("Número:", contador)
    contador += 1
