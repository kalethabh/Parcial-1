class ProgramFidelity:
    def __init__(self, ID, nombre, descripcion, tipo, vigencia, puntos_fidelizacion):
        """
        Constructor de la clase ProgramFidelity que recibe como parámetros:

        :param ID: Identificador del programa de fidelización
        :param nombre: Nombre del programa de fidelización
        :param descripcion: Descripción del programa de fidelización
        :param tipo: Tipo del programa de fidelización
        :param vigencia: Fecha de vigencia del programa de fidelización
        :param puntos_fidelizacion: Puntos de fidelización del programa
        """
        self.ID = ID
        self.nombre = nombre
        self.descripcion = descripcion
        self.tipo = tipo
        self.vigencia = vigencia
        self.puntos_fidelizacion = puntos_fidelizacion

    @property
    def ID(self):
        """
        Getter del ID del programa de fidelización
        """
        return self._ID

    @ID.setter
    def ID(self, value):
        """
        Setter del ID del programa de fidelización
        """
        self._ID = value

    @property
    def nombre(self):
        """
        Getter del nombre del programa de fidelización
        """
        return self._nombre

    @nombre.setter
    def nombre(self, value):
        """
        Setter del nombre del programa de fidelización
        """
        self._nombre = value

    @property
    def descripcion(self):
        """
        Getter de la descripción del programa de fidelización
        """
        return self._descripcion

    @descripcion.setter
    def descripcion(self, value):
        """
        Setter de la descripción del programa de fidelización
        """
        self._descripcion = value

    @property
    def tipo(self):
        """
        Getter del tipo del programa de fidelización
        """
        return self._tipo

    @tipo.setter
    def tipo(self, value):
        """
        Setter del tipo del programa de fidelización
        """
        self._tipo = value

    @property
    def vigencia(self):
        """
        Getter de la fecha de vigencia del programa de fidelización
        """
        return self._vigencia

    @vigencia.setter
    def vigencia(self, value):
        """
        Setter de la fecha de vigencia del programa de fidelización
        """
        self._vigencia = value

    @property
    def puntos_fidelizacion(self):
        """
        Getter de los puntos de fidelización del programa
        """
        return self._puntos_fidelizacion

    @puntos_fidelizacion.setter
    def puntos_fidelizacion(self, value):
        """
        Setter de los puntos de fidelización del programa
        """
        self._puntos_fidelizacion = value
