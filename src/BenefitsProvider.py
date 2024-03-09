class BenefitsProvider:
    def __init__(self, id, name, benefit_types):
        """
        Constructor de la clase BenefitsProvider que recibe como parámetros:

        :param id: Identificador del proveedor de beneficios
        :param name: Nombre del proveedor de beneficios
        :param benefit_types: Tipos de beneficios ofrecidos por el proveedor
        """
        self.id = id
        self.name = name
        self.benefit_types = benefit_types

    def add_provider(self):
        """
        Método para agregar un nuevo proveedor de beneficios
        """
        pass

    def __str__(self):
        """
        Método para representar el objeto como una cadena de texto
        """
        return f"Provider ID: {self.id}, Name: {self.name}"
