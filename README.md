# Parcial-1

En una era donde la tecnología redefine constantemente las expectativas de los consumidores, una empresa emergente visionaria se embarcó en una misión para revolucionar la forma en que las personas interactúan con y aprovechan sus múltiples beneficios financieros y de servicios. Inspirados por la complejidad que enfrentaban los usuarios al gestionar sus beneficios dispersos en seguros, tarjetas de crédito, y programas de fidelización, el equipo se propuso construir un sistema unificado que no solo centralizara estos beneficios en una sola plataforma, sino que también orientara a los usuarios hacia la maximización de su valor en cada compra. Este sistema integrado de beneficios se convirtió en la piedra angular de su visión, prometiendo una interfaz intuitiva respaldada por una arquitectura robusta y un motor de recomendaciones inteligente.

Al abordar el diseño del sistema, la elección de una arquitectura de microservicios emergió como la solución óptima, promoviendo la flexibilidad, la escalabilidad y la facilidad de integración con sistemas externos. Esta arquitectura facilitaría la actualización y expansión continuas del sistema, permitiendo al equipo añadir nuevos proveedores de beneficios o actualizar los existentes sin interrupciones significativas.

Por otra parte, la identificación de los requerimientos críticos, equilibrando cuidadosamente las necesidades funcionales, como la integración transparente con diversos proveedores de beneficios y un sistema de recomendaciones altamente personalizado, con imperativos no funcionales como seguridad de datos, escalabilidad y disponibilidad. La meta es crear un sistema que no solo respondiera a las necesidades actuales de los usuarios, sino que también pudiera adaptarse a las demandas futuras.

La presentación clara de los beneficios disponibles, junto con una retroalimentación inmediata y relevante sobre las recomendaciones de beneficios, se convirtió en una prioridad para asegurar que los usuarios pudieran tomar decisiones informadas con facilidad. Así mismo, con los cimientos tecnológicos en su lugar, la experiencia del usuario debe ser visualmente atractiva y accesible en una variedad de dispositivos, si no que también proporcionara una interacción intuitiva con el sistema.

La implementación del sistema debe seguir los principios SOLID para asegurar un código mantenible y extensible. Cada microservicio debe ser construido con un propósito específico, desde gestionar la autenticación de usuarios hasta procesar complejas recomendaciones de beneficios. La seguridad fue debe estar en cada etapa empleando las mejores prácticas para proteger la información personal y financiera de los usuarios.
![img](https://github.com/kalethabh/Parcial-1/assets/113316840/ba8027f1-7b37-4521-97dd-d5d12534718b)
### Single Responsibility Principle (Principio de Responsabilidad Única)

En nuestro diagrama de clases, cada clase cumple con el principio de responsabilidad única al tener una sola razón para cambiar. Por ejemplo:

- La clase `User` se encarga exclusivamente de la gestión de usuarios.
- La clase `CreditCard` se ocupa únicamente de la gestión de tarjetas de crédito.
- La clase `Customer` tiene la responsabilidad exclusiva de representar a un cliente en el sistema.

### Open/Closed Principle (Principio de Abierto/Cerrado)

Este principio se cumple en nuestro diseño al utilizar interfaces o clases abstractas para permitir la extensión sin necesidad de modificar el código existente. Por ejemplo:

- Podemos añadir nuevos métodos de autenticación implementando la interfaz `Authenticator` sin necesidad de modificar el código existente en otras clases.
- Podemos añadir nuevos tipos de beneficios financieros implementando la interfaz `FinancialBenefits` sin modificar las clases existentes.

### Substitution Principle (Principio de Sustitución de Liskov)

Este principio se cumple en nuestro diseño al garantizar que las subclases puedan ser utilizadas a través de referencias a la clase base sin alterar el comportamiento esperado. Por ejemplo:

- Las subclases de `User`, como `Customer`, pueden ser utilizadas en lugar de la clase base `User` sin cambiar el comportamiento esperado en otras partes del sistema.

### Interface Segregation Principle (Principio de Segregación de Interfaces)

Este principio se cumple en nuestro diseño al separar las interfaces grandes en interfaces más específicas y pequeñas para evitar que los clientes dependan de interfaces que no usan. Por ejemplo:

- Tenemos interfaces separadas para la gestión de usuarios, gestión de tarjetas de crédito, gestión de beneficios, etc., lo que permite a los clientes interactuar con las interfaces relevantes para sus necesidades sin depender de funcionalidades innecesarias.

### Dependency Inversion Principle (Principio de Inversión de Dependencias)

Este principio se cumple en nuestro diseño al asegurarnos de que los módulos de alto nivel no dependan directamente de los módulos de bajo nivel, y que ambos dependan de abstracciones. Por ejemplo:

- La lógica de alto nivel, como la gestión de usuarios, depende de interfaces como `User` en lugar de depender directamente de las implementaciones concretas de las clases.

---
![Diagrama oo (2)](https://github.com/kalethabh/Parcial-1/assets/113316840/8afc2ab9-ccb8-4470-8ecf-f82648777692)

