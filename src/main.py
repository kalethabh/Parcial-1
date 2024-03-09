from user import User
from personal_information import PersonalInformation
from credit_card import CreditCard
from client import Client
from credentials import Credentials
from authenticator import Authenticator
from benefits import Benefits
from program_fidelity import ProgramFidelity
from benefits_provider import BenefitsProvider
from financial_benefits import FinancialBenefits
from service_benefits import ServiceBenefits
from service_type import ServiceType
from activity_record import ActivityRecord

def main():
    usuario = User(cedula=123456789, nombre="Juan")
    informacion_personal = PersonalInformation(
        nombre_completo="Juan Pérez",
        fecha_nacimiento=datetime(1990, 1, 1),
        direccion="123 Calle Principal",
        numero_telefono="1234567890",
        nacionalidad="Mexicana"
    )
    tarjeta_credito = CreditCard(
        numero="1234567890123456",
        fecha_expiracion="12/24",
        cvv="123",
        usuario=usuario
    )
    cliente = Client(cedula="987654321", nombre="Cliente")
    credenciales = Credentials(nombre_usuario="user123", contraseña="password")
    autenticador = Authenticator(credenciales)
    beneficios = Benefits()
    programa_fidelizacion = ProgramFidelity(
        id=1,
        nombre="Programa1",
        descripcion="Descripción del programa",
        tipo="Tipo1",
        vigencia=datetime(2024, 12, 31),
        puntos_fidelizacion=100
    )
    proveedor_beneficios = BenefitsProvider(
        id=1,
        nombre="Proveedor1",
        tipo_beneficios=["Tipo1", "Tipo2"]
    )
    beneficios_financieros = FinancialBenefits(
        tasa_interes=0.05,
        plazo=12,
        tipo_interes="Tasa Fija"
    )
    beneficios_servicios = ServiceBenefits(
        id=1,
        nombre="Servicio1",
        tipo="Tipo1",
        proveedor_beneficios=proveedor_beneficios,
        lista_beneficios=["Beneficio1", "Beneficio2"]
    )
    tipo_servicio = ServiceType(
        id=1,
        nombre="Servicio1",
        descripcion="Descripción del servicio"
    )
    registro_actividad = ActivityRecord(attribute1="value1", attribute2="value2", attribute3="value3")

    print("Ejemplo de uso de las clases definidas.")


if __name__ == "__main__":
    main()