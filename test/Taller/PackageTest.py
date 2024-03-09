import unittest
from user import User
from service_type import ServiceType
from service_benefits import ServiceBenefits
from program_fidelity import ProgramFidelity
from personal_information import PersonalInformation
from interface_user import InterfaceUser
from benefits import Benefits
from benefits_provider import BenefitsProvider
from financial_benefits import FinancialBenefits
from service_benefits import ServiceBenefits
from credit_card import CreditCard
from authenticator import Authenticator
from financial_benefits_management import FinancialBenefitsManagement


class TestUser(unittest.TestCase):

    def test_constructor(self):
        user = User(cedula=1234567890, nombre="John Doe")
        self.assertEqual(user.cedula, 1234567890)
        self.assertEqual(user.nombre, "John Doe")
        self.assertIsNone(user.correoElectronico)
        self.assertIsNone(user.informacionPersonal)

    def test_registrar(self):
        user = User(cedula=1234567890, nombre="John Doe")
        user.registrar()

    def test_iniciar_sesion(self):
        user = User(cedula=1234567890, nombre="John Doe")
        user.iniciar_sesion()

    def test_obtener_informacion_personal(self):
        user = User(cedula=1234567890, nombre="John Doe")
        informacion_personal = user.obtener_informacion_personal()

class TestServiceType(unittest.TestCase):

    def test_constructor(self):
        service_type = ServiceType(ID=1, nombre="Servicio de envío", descripcion="Envío de paquetes")
        self.assertEqual(service_type.ID, 1)
        self.assertEqual(service_type.nombre, "Servicio de envío")
        self.assertEqual(service_type.descripcion, "Envío de paquetes")

    def test_crear_servicio(self):
        service_type = ServiceType(ID=1, nombre="Servicio de envío", descripcion="Envío de paquetes")
        servicio = service_type.crear_servicio()

class TestServiceBenefits(unittest.TestCase):

    def test_constructor(self):
        service_benefits = ServiceBenefits(ID=1, nombre="Descuento por volumen", descripcion="Descuento aplicado a grandes volúmenes de envío")
        self.assertEqual(service_benefits.ID, 1)
        self.assertEqual(service_benefits.nombre, "Descuento por volumen")
        self.assertEqual(service_benefits.descripcion, "Descuento aplicado a grandes volúmenes de envío")

    def test_obtener_beneficios(self):
        service_benefits = ServiceBenefits(ID=1, nombre="Descuento por volumen", descripcion="Descuento aplicado a grandes volúmenes de envío")
        beneficios = service_benefits.obtener_beneficios()

class TestProgramFidelity(unittest.TestCase):

    def test_constructor(self):
        program_fidelity = ProgramFidelity(id=1, nombre="Programa de puntos", descripcion="Programa de puntos para clientes frecuentes", tipo="Puntos", vigencia="2024-12-31", puntos_fidelizacion=100)
        self.assertEqual(program_fidelity.id, 1)
        self.assertEqual(program_fidelity.nombre, "Programa de puntos")
        self.assertEqual(program_fidelity.descripcion, "Programa de puntos para clientes frecuentes")
        self.assertEqual(program_fidelity.tipo, "Puntos")
        self.assertEqual(program_fidelity.vigencia, "2024-12-31")
        self.assertEqual(program_fidelity.puntos_fidelizacion, 100)

    def test_actualizar_puntos_fidelizacion(self):
        program_fidelity = ProgramFidelity(id=1, nombre="Programa de puntos", descripcion="Programa de puntos para clientes frecuentes", tipo="Puntos", vigencia="2024-12-31", puntos_fidelizacion=100)
        program_fidelity.actualizar_puntos_fidelizacion(150)
        self.assertEqual(program_fidelity.puntos_fidelizacion, 150)

class TestPersonalInformation(unittest.TestCase):

    def test_constructor(self):
        personal_info = PersonalInformation(nombre_completo="Juan Perez", fecha_nacimiento="1990-05-15", direccion="Calle 123", numero_telefono="123456789", nacionalidad="Mexicana")
        self.assertEqual(personal_info.nombre_completo, "Juan Perez")
        self.assertEqual(personal_info.fecha_nacimiento, "1990-05-15")
        self.assertEqual(personal_info.direccion, "Calle 123")
        self.assertEqual(personal_info.numero_telefono, "123456789")
        self.assertEqual(personal_info.nacionalidad, "Mexicana")

    def test_actualizar_informacion(self):
        personal_info = PersonalInformation(nombre_completo="Juan Perez", fecha_nacimiento="1990-05-15", direccion="Calle 123", numero_telefono="123456789", nacionalidad="Mexicana")
        personal_info.actualizar_informacion(direccion="Avenida 456", numero_telefono="987654321")
        self.assertEqual(personal_info.direccion, "Avenida 456")
        self.assertEqual(personal_info.numero_telefono, "987654321")

class TestInterfaceUser(unittest.TestCase):

    def test_constructor(self):
        interface_user = InterfaceUser(attribute1="value1", attribute2="value2", attribute3="value3")
        self.assertEqual(interface_user.attribute1, "value1")
        self.assertEqual(interface_user.attribute2, "value2")
        self.assertEqual(interface_user.attribute3, "value3")

    def test_operation1(self):
        interface_user = InterfaceUser()
        result = interface_user.operation1(5)
        self.assertEqual(result, 5)

    def test_operation2(self):
        interface_user = InterfaceUser()
        result = interface_user.operation2("test")
        self.assertEqual(result, "test")

class TestBenefits(unittest.TestCase):

    def test_obtener_beneficios_de_servicio(self):
        beneficios = Benefits()
        beneficios_servicio = beneficios.obtener_beneficios_de_servicio()
        self.assertIsNotNone(beneficios_servicio)
        self.assertIsInstance(beneficios_servicio, list)

    def test_obtener_beneficios_financieros(self):
        beneficios = Benefits()
        beneficios_financieros = beneficios.obtener_beneficios_financieros()
        self.assertIsNotNone(beneficios_financieros)
        self.assertIsInstance(beneficios_financieros, list)

    def test_obtener_programa_fidelizacion(self):
        beneficios = Benefits()
        programa_fidelizacion = beneficios.obtener_programa_fidelizacion()
        self.assertIsNotNone(programa_fidelizacion)
        self.assertIsInstance(programa_fidelizacion, dict)

class TestBenefitsProvider(unittest.TestCase):

    def test_constructor(self):
        provider = BenefitsProvider(1, "Proveedor de Beneficios", ["Beneficio 1", "Beneficio 2"])
        self.assertIsNotNone(provider)
        self.assertEqual(provider.id, 1)
        self.assertEqual(provider.nombre, "Proveedor de Beneficios")
        self.assertEqual(provider.tipo_beneficios, ["Beneficio 1", "Beneficio 2"])

    def test_agregar_proveedor(self):
        provider = BenefitsProvider(1, "Proveedor de Beneficios", [])
        self.assertEqual(len(provider.tipo_beneficios), 0)

        provider.agregar_proveedor("Nuevo Beneficio")
        self.assertEqual(len(provider.tipo_beneficios), 1)
        self.assertEqual(provider.tipo_beneficios[0], "Nuevo Beneficio")

class TestFinancialBenefits(unittest.TestCase):

    def test_constructor(self):
        benefits = FinancialBenefits(1, "Beneficios Financieros", 0.05, 12, "Tasa Fija")
        self.assertIsNotNone(benefits)
        self.assertEqual(benefits.id, 1)
        self.assertEqual(benefits.nombre, "Beneficios Financieros")
        self.assertEqual(benefits.tasa_interes, 0.05)
        self.assertEqual(benefits.plazo, 12)
        self.assertEqual(benefits.tipo_interes, "Tasa Fija")

    def test_crear_beneficio(self):
        benefits = FinancialBenefits(1, "Beneficios Financieros", 0.05, 12, "Tasa Fija")
        self.assertEqual(len(benefits.lista_beneficios), 0)

        benefits.crear_beneficio("Nuevo Beneficio")
        self.assertEqual(len(benefits.lista_beneficios), 1)
        self.assertEqual(benefits.lista_beneficios[0], "Nuevo Beneficio")

class TestServiceBenefits(unittest.TestCase):

    def test_constructor(self):
        benefits = ServiceBenefits(1, "Beneficios de Servicios", "Servicio Premium", "Proveedor A")
        self.assertIsNotNone(benefits)
        self.assertEqual(benefits.id, 1)
        self.assertEqual(benefits.nombre, "Beneficios de Servicios")
        self.assertEqual(benefits.tipo, "Servicio Premium")
        self.assertEqual(benefits.proveedor, "Proveedor A")

    def test_obtener_beneficios(self):
        benefits = ServiceBenefits(1, "Beneficios de Servicios", "Servicio Premium", "Proveedor A")
        self.assertEqual(len(benefits.obtener_beneficios()), 0)

        benefits.agregar_beneficio("Descuento en envíos")
        benefits.agregar_beneficio("Atención al cliente prioritaria")

        self.assertEqual(len(benefits.obtener_beneficios()), 2)
        self.assertIn("Descuento en envíos", benefits.obtener_beneficios())
        self.assertIn("Atención al cliente prioritaria", benefits.obtener_beneficios())

class TestCreditCard(unittest.TestCase):

    def test_constructor(self):
        user = User("123456789", "John", "Doe", "john@example.com")
        credit_card = CreditCard("1234567890123456", "12/24", "123", user)
        self.assertEqual(credit_card.numero, "1234567890123456")
        self.assertEqual(credit_card.fecha_expiracion, "12/24")
        self.assertEqual(credit_card.cvv, "123")
        self.assertEqual(credit_card.usuario, user)

class TestAuthenticator(unittest.TestCase):

    def setUp(self):
        self.credentials = {"user1": "password1", "user2": "password2"}
        self.db = self.credentials.copy()
        self.authenticator = Authenticator(self.credentials, self.db)

    def test_autenticar_usuario_valido(self):
        self.assertTrue(self.authenticator.autenticar("user1", "password1"))

    def test_autenticar_usuario_invalido(self):
        self.assertFalse(self.authenticator.autenticar("user3", "password3"))

    def test_autenticar_contraseña_invalida(self):
        self.assertFalse(self.authenticator.autenticar("user2", "password3"))
        
class TestFinancialBenefitsManagement(unittest.TestCase):

    def setUp(self):
        self.benefits_management = FinancialBenefitsManagement()
        self.benefit1 = FinancialBenefits("Descuento en préstamos", 0.2)
        self.benefit2 = FinancialBenefits("Tarifas preferenciales en cuentas de ahorro", 0.1)

    def test_agregar_beneficio_financiero(self):
        self.benefits_management.agregar_beneficio_financiero(self.benefit1)
        self.assertIn(self.benefit1, self.benefits_management.benefits)

    def test_eliminar_beneficio_financiero(self):
        self.benefits_management.agregar_beneficio_financiero(self.benefit1)
        self.benefits_management.eliminar_beneficio_financiero(self.benefit1)
        self.assertNotIn(self.benefit1, self.benefits_management.benefits)

    def test_listar_beneficios_financieros(self):
        self.benefits_management.agregar_beneficio_financiero(self.benefit1)
        self.benefits_management.agregar_beneficio_financiero(self.benefit2)
        self.assertEqual(len(self.benefits_management.benefits), 2)
        # Aquí se debería redirigir la salida estándar y comprobar que se imprimen los beneficios correctamente.

    def test_buscar_beneficio_financiero_existente(self):
        self.benefits_management.agregar_beneficio_financiero(self.benefit1)
        self.assertEqual(self.benefits_management.buscar_beneficio_financiero("Descuento en préstamos"), self.benefit1)

    def test_buscar_beneficio_financiero_inexistente(self):
        self.assertIsNone(self.benefits_management.buscar_beneficio_financiero("Descuento en tarjetas de crédito"))

if __name__ == '__main__':
    unittest.main()
