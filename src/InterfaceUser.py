from abc import ABC, abstractmethod

class InterfaceUser(ABC):
    def __init__(self, attribute1, attribute2, attribute3):
        """
        Constructor de la clase InterfaceUser que recibe como parámetros:

        :param attribute1: Atributo 1 de la interfaz
        :param attribute2: Atributo 2 de la interfaz
        :param attribute3: Atributo 3 de la interfaz
        """
        self.attribute1 = attribute1
        self.attribute2 = attribute2
        self.attribute3 = attribute3

    @abstractmethod
    def operation1(self, params):
        """
        Método abstracto operation1 de la interfaz

        :param params: Parámetros del método
        :return: Tipo de retorno del método
        """
        pass

    @abstractmethod
    def operation2(self, params):
        """
        Método abstracto operation2 de la interfaz

        :param params: Parámetros del método
        """
        pass

    @abstractmethod
    def operation3(self):
        """
        Método abstracto operation3 de la interfaz
        """
        pass
