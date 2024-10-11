# main.py
from mi_clase import MiClase
from claseAlumno import Alumno

# Crear una instancia de la clase
persona = MiClase("Carlos")

# Llamar a un método de la clase
persona.saludar()

#Clase Alumno
#Crea la instancia de alumno
alumno = Alumno()

# Asignar valores utilizando el método set_datos
alumno.set_datos("Juan", "Pérez", "García", "12345", "3")

# Obtener valores usando los getters
print("Nombre:", alumno.get_nombre())  # Juan
print("Apellido paterno:", alumno.get_apellido_paterno())  # Pérez
print("Apellido materno:", alumno.get_apellido_materno())  # García
print("Nombre completo:", alumno.get_nombre_completo())  # Juan Pérez García
print("Número de control:", alumno.get_no_control())  # 12345
print("Semestre:", alumno.get_semestre())  # 3

# Diccionario para almacenar los alumnos
registro_alumnos = {}

for i in range(3):
    print(f"\nCapturando datos del alumno {i + 1}:")

    alumno = Alumno()  # Crear una nueva instancia de Alumno

    # Utilizar el método set_datos para capturar los datos de un alumno
    nombre = input("Ingresa el nombre: ")
    apellido_paterno = input("Ingresa el apellido paterno: ")
    apellido_materno = input("Ingresa el apellido materno: ")
    no_control = input("Ingresa el número de control: ")
    semestre = int(input("Ingresa el semestre: "))

    alumno.set_datos(nombre, apellido_paterno, apellido_materno, no_control, semestre)

    # Guardar en el diccionario de alumnos usando el número de registro como clave
    registro_alumnos[i] = {
        "nombre": alumno.get_nombre_completo(),
        "semestre": alumno.get_semestre()
    }

# Mostrar el registro de alumnos
print("\nRegistro de alumnos:")
for registro, datos in registro_alumnos.items():
    print(f"Registro: {registro} - Nombre: {datos['nombre']} (Semestre: {datos['semestre']})")
