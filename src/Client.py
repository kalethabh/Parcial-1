class Client:
    def __init__(self, id, name, benefits):
        """
        Constructor de la clase Client que recibe como parámetros:

        :param id: Identificador del cliente
        :param name: Nombre del cliente
        :param benefits: Beneficios asociados al cliente
        """
        self.id = id
        self.name = name
        self.benefits = benefits

    def register_activity(self):
        """
        Método para registrar actividad del cliente
        """
        pass

    def __str__(self):
        """
        Método para representar el objeto como una cadena de texto
        """
        return f"Client ID: {self.id}, Name: {self.name}"
