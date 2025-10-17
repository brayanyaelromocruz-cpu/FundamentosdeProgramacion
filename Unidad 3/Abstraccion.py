from abc import ABC, abstractmethod

# Clase abstracta
class Vehiculo(ABC):
    def __init__(self, marca, modelo, año, color):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.color = color

    def __str__(self):
        return f"Vehículo genérico: {self.marca} {self.modelo} ({self.año}) - Color: {self.color}"


# Subclases que heredan solo los atributos
class Auto(Vehiculo):
    pass


class Moto(Vehiculo):
    pass


class Camion(Vehiculo):
    pass

#Nueva clase agregada
class Avion(Vehiculo):
    pass


# Crear objetos de las clases hijas
auto1 = Auto("Toyota", "Corolla", 2022, "Rojo")
moto1 = Moto("Yamaha", "FZ", 2021, "Negra")
camion1 = Camion("Volvo", "FH", 2020, "Blanco")

# Nuevas instancias 
bici1 = OtroVehiculo("Giant", "Escape 3", 2022, "Verde")
bici_elec1 = OtroVehiculo("Specialized", "Turbo Vado", 2023, "Negra")
patineta1 = OtroVehiculo("Razor", "A5 Lux", 2021, "Roja")
scooter1 = OtroVehiculo("Xiaomi", "Mi Electric", 2022, "Gris")
tractor1 = OtroVehiculo("John Deere", "5050E", 2020, "Verde")
lancha1 = OtroVehiculo("Yamaha", "212X", 2019, "Blanca")
heli1 = OtroVehiculo("Bell", "206", 2018, "Azul")
tren1 = OtroVehiculo("Siemens", "Velaro", 2024, "Plata")

# los nuevos vehículos
print(bici1)
print(bici_elec1)
print(patineta1)
print(scooter1)
print(tractor1)
print(lancha1)
print(heli1)
print(tren1)