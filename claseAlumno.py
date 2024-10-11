class Alumno:
    def __init__(self):
        # Crea la función constructor con atributos vacíos
        self.__nombre = None
        self.__apellido_paterno = None
        self.__apellido_materno = None
        self.__no_control = None
        self.__semestre = None

    # Método para asignar todos los valores de una vez
    def set_datos(self, nombre, apellido_paterno, apellido_materno, no_control, semestre):
        self.set_nombre(nombre)
        self.set_apellido_paterno(apellido_paterno)
        self.set_apellido_materno(apellido_materno)
        self.set_no_control(no_control)
        self.set_semestre(semestre)

    # Métodos para asignar valores (setters)
    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_apellido_paterno(self, apellido_paterno):
        self.__apellido_paterno = apellido_paterno

    def set_apellido_materno(self, apellido_materno):
        self.__apellido_materno = apellido_materno

    def set_no_control(self, no_control):
        self.__no_control = no_control

    def set_semestre(self, semestre):
        self.__semestre = semestre

    # Métodos para obtener los valores (getters)
    def get_nombre(self):
        return self.__nombre

    def get_apellido_paterno(self):
        return self.__apellido_paterno

    def get_apellido_materno(self):
        return self.__apellido_materno

    def get_no_control(self):
        return self.__no_control

    def get_semestre(self):
        return self.__semestre

    # Nombre completo
    def get_nombre_completo(self):
        return f"{self.__nombre} {self.__apellido_paterno} {self.__apellido_materno}"