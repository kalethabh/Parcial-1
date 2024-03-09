class User:
    def __init__(self, cedula, nombre, correo_electronico, informacion_personal):
        """
        Constructor de la clase User que recibe como parámetros:

        :param cedula:
        :param nombre:
        :param correo_electronico:
        :param informacion_personal:
        """
        self.cedula = cedula
        self.nombre = nombre
        self.correo_electronico = correo_electronico
        self.informacion_personal = informacion_personal

    @property
    def cedula(self):
        """
        Getter de cedula
        :return: cedula
        """
        return self._cedula

    @cedula.setter
    def cedula(self, value):
        """
        Setter de cedula que recibe como parámetro:
        :param value:
        """
        self._cedula = value

    @property
    def nombre(self):
        """
        Getter de nombre
        :return: nombre
        """
        return self._nombre

    @nombre.setter
    def nombre(self, value):
        """
        Setter de nombre que recibe como parámetro:
        :param value:
        """
        self._nombre = value

    @property
    def correo_electronico(self):
        """
        Getter de correo_electronico
        :return: correo_electronico
        """
        return self._correo_electronico

    @correo_electronico.setter
    def correo_electronico(self, value):
        """
        Setter de correo_electronico que recibe como parámetro:
        :param value:
        """
        self._correo_electronico = value

    @property
    def informacion_personal(self):
        """
        Getter de informacion_personal
        :return: informacion_personal
        """
        return self._informacion_personal

    @informacion_personal.setter
    def informacion_personal(self, value):
        """
        Setter de informacion_personal que recibe como parámetro:
        :param value:
        """
        self._informacion_personal = value

    def registrar(self):
        """
        Método para registrar al usuario
        """
        # Lógica para registrar al usuario

    def iniciar_sesion(self):
        """
        Método para iniciar sesión del usuario
        """
        # Lógica para iniciar sesión del usuario

    def obtener_informacion_personal(self):
        """
        Método para obtener información personal
        """
        # Lógica para obtener información personal del usuario
