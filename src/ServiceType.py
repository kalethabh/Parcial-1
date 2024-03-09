class ServiceType:
    def __init__(self, ID, nombre, descripcion):
        """
        Constructor de la clase ServiceType que recibe como parámetros:

        :param ID: Identificador del tipo de servicio
        :param nombre: Nombre del tipo de servicio
        :param descripcion: Descripción del tipo de servicio
        """
        self.ID = ID
        self.nombre = nombre
        self.descripcion = descripcion

    @property
    def ID(self):
        """
        Getter del ID del tipo de servicio
        """
        return self._ID

    @ID.setter
    def ID(self, value):
        """
        Setter del ID del tipo de servicio
        """
        self._ID = value

    @property
    def nombre(self):
        """
        Getter del nombre del tipo de servicio
        """
        return self._nombre

    @nombre.setter
    def nombre(self, value):
        """
        Setter del nombre del tipo de servicio
        """
        self._nombre = value

    @property
    def descripcion(self):
        """
        Getter de la descripción del tipo de servicio
        """
        return self._descripcion

    @descripcion.setter
    def descripcion(self, value):
        """
        Setter de la descripción del tipo de servicio
        """
        self._descripcion = value

    def crear_servicio(self):
        """
        Método para crear un nuevo servicio
        """
        # Lógica para crear un nuevo servicio
