class ServiceBenefits:
    def __init__(self, ID, nombre, tipo, proveedor_beneficios, lista_beneficios):
        """
        Constructor de la clase ServiceBenefits que recibe como parámetros:

        :param ID: Identificador del servicio de beneficios
        :param nombre: Nombre del servicio de beneficios
        :param tipo: Tipo del servicio de beneficios
        :param proveedor_beneficios: Proveedor del servicio de beneficios
        :param lista_beneficios: Lista de beneficios del servicio
        """
        self.ID = ID
        self.nombre = nombre
        self.tipo = tipo
        self.proveedor_beneficios = proveedor_beneficios
        self.lista_beneficios = lista_beneficios

    @property
    def ID(self):
        """
        Getter del ID del servicio de beneficios
        """
        return self._ID

    @ID.setter
    def ID(self, value):
        """
        Setter del ID del servicio de beneficios
        """
        self._ID = value

    @property
    def nombre(self):
        """
        Getter del nombre del servicio de beneficios
        """
        return self._nombre

    @nombre.setter
    def nombre(self, value):
        """
        Setter del nombre del servicio de beneficios
        """
        self._nombre = value

    @property
    def tipo(self):
        """
        Getter del tipo del servicio de beneficios
        """
        return self._tipo

    @tipo.setter
    def tipo(self, value):
        """
        Setter del tipo del servicio de beneficios
        """
        self._tipo = value

    @property
    def proveedor_beneficios(self):
        """
        Getter del proveedor del servicio de beneficios
        """
        return self._proveedor_beneficios

    @proveedor_beneficios.setter
    def proveedor_beneficios(self, value):
        """
        Setter del proveedor del servicio de beneficios
        """
        self._proveedor_beneficios = value

    @property
    def lista_beneficios(self):
        """
        Getter de la lista de beneficios del servicio de beneficios
        """
        return self._lista_beneficios

    @lista_beneficios.setter
    def lista_beneficios(self, value):
        """
        Setter de la lista de beneficios del servicio de beneficios
        """
        self._lista_beneficios = value
