class CreditCard:
    def __init__(self, number, expiration_date, cvv, user):
        """
        Constructor de la clase CreditCard que recibe como parámetros:

        :param number: Número de tarjeta de crédito
        :param expiration_date: Fecha de expiración
        :param cvv: Código de seguridad (CVV)
        :param user: Usuario asociado a la tarjeta de crédito
        """
        self.number = number
        self.expiration_date = expiration_date
        self.cvv = cvv
        self.user = user

    def process_payment(self, amount):
        """
        Método para procesar un pago con la tarjeta de crédito

        :param amount: Monto del pago
        """
        pass

    def validate_credit_limit(self, amount):
        """
        Método para validar el límite de crédito disponible

        :param amount: Monto del pago a validar
        :return: True si el límite es suficiente, False en caso contrario
        """
        pass
