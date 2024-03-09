class PersonalInformation:
    def __init__(self, nombre_completo, fecha_nacimiento, direccion, numero_telefono, nacionalidad):
        """
        Constructor de la clase PersonalInformation que recibe como parámetros:

        :param nombre_completo: Nombre completo de la persona
        :param fecha_nacimiento: Fecha de nacimiento de la persona
        :param direccion: Dirección de la persona
        :param numero_telefono: Número de teléfono de la persona
        :param nacionalidad: Nacionalidad de la persona
        """
        self.nombre_completo = nombre_completo
        self.fecha_nacimiento = fecha_nacimiento
        self.direccion = direccion
        self.numero_telefono = numero_telefono
        self.nacionalidad = nacionalidad

    @property
    def nombre_completo(self):
        """
        Getter del nombre completo de la persona
        """
        return self._nombre_completo

    @nombre_completo.setter
    def nombre_completo(self, value):
        """
        Setter del nombre completo de la persona
        """
        self._nombre_completo = value

    @property
    def fecha_nacimiento(self):
        """
        Getter de la fecha de nacimiento de la persona
        """
        return self._fecha_nacimiento

    @fecha_nacimiento.setter
    def fecha_nacimiento(self, value):
        """
        Setter de la fecha de nacimiento de la persona
        """
        self._fecha_nacimiento = value

    @property
    def direccion(self):
        """
        Getter de la dirección de la persona
        """
        return self._direccion

    @direccion.setter
    def direccion(self, value):
        """
        Setter de la dirección de la persona
        """
        self._direccion = value

    @property
    def numero_telefono(self):
        """
        Getter del número de teléfono de la persona
        """
        return self._numero_telefono

    @numero_telefono.setter
    def numero_telefono(self, value):
        """
        Setter del número de teléfono de la persona
        """
        self._numero_telefono = value

    @property
    def nacionalidad(self):
        """
        Getter de la nacionalidad de la persona
        """
        return self._nacionalidad

    @nacionalidad.setter
    def nacionalidad(self, value):
        """
        Setter de la nacionalidad de la persona
        """
        self._nacionalidad = value
