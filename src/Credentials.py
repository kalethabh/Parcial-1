class Credentials:
    def __init__(self, username, password):
        """
        Constructor de la clase Credentials que recibe como parámetros:

        :param username: Nombre de usuario
        :param password: Contraseña
        """
        self.username = username
        self.password = password

    def create_user(self):
        """
        Método para crear un nuevo usuario
        """
        pass

    def authenticate(self):
        """
        Método para autenticar al usuario

        :return: True si la autenticación es exitosa, False en caso contrario
        """
        pass
