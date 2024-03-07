# Parcial-1

En una era donde la tecnología redefine constantemente las expectativas de los consumidores, una empresa emergente visionaria se embarcó en una misión para revolucionar la forma en que las personas interactúan con y aprovechan sus múltiples beneficios financieros y de servicios. Inspirados por la complejidad que enfrentaban los usuarios al gestionar sus beneficios dispersos en seguros, tarjetas de crédito, y programas de fidelización, el equipo se propuso construir un sistema unificado que no solo centralizara estos beneficios en una sola plataforma, sino que también orientara a los usuarios hacia la maximización de su valor en cada compra. Este sistema integrado de beneficios se convirtió en la piedra angular de su visión, prometiendo una interfaz intuitiva respaldada por una arquitectura robusta y un motor de recomendaciones inteligente.

Al abordar el diseño del sistema, la elección de una arquitectura de microservicios emergió como la solución óptima, promoviendo la flexibilidad, la escalabilidad y la facilidad de integración con sistemas externos. Esta arquitectura facilitaría la actualización y expansión continuas del sistema, permitiendo al equipo añadir nuevos proveedores de beneficios o actualizar los existentes sin interrupciones significativas.

Por otra parte, la identificación de los requerimientos críticos, equilibrando cuidadosamente las necesidades funcionales, como la integración transparente con diversos proveedores de beneficios y un sistema de recomendaciones altamente personalizado, con imperativos no funcionales como seguridad de datos, escalabilidad y disponibilidad. La meta es crear un sistema que no solo respondiera a las necesidades actuales de los usuarios, sino que también pudiera adaptarse a las demandas futuras.

La presentación clara de los beneficios disponibles, junto con una retroalimentación inmediata y relevante sobre las recomendaciones de beneficios, se convirtió en una prioridad para asegurar que los usuarios pudieran tomar decisiones informadas con facilidad. Así mismo, con los cimientos tecnológicos en su lugar, la experiencia del usuario debe ser visualmente atractiva y accesible en una variedad de dispositivos, si no que también proporcionara una interacción intuitiva con el sistema.

La implementación del sistema debe seguir los principios SOLID para asegurar un código mantenible y extensible. Cada microservicio debe ser construido con un propósito específico, desde gestionar la autenticación de usuarios hasta procesar complejas recomendaciones de beneficios. La seguridad fue debe estar en cada etapa empleando las mejores prácticas para proteger la información personal y financiera de los usuarios.
![img](https://github.com/kalethabh/Parcial-1/assets/113316840/ba8027f1-7b37-4521-97dd-d5d12534718b)
![Diagrama arquitectura](https://github.com/kalethabh/Parcial-1/assets/113316840/ea550db8-c495-4f7f-a3a9-00130fada740)


## Single Responsibility Principle (SRP - Principio de Responsabilidad Única):

- **User**: Esta clase parece estar relacionada con la gestión de usuarios y la información personal. Se encarga de la autenticación de usuarios y el manejo de su información personal. Cumple con el principio de responsabilidad única al manejar las responsabilidades relacionadas con la gestión del usuario.
- **InterfazUsuario**: Esta clase parece ser una interfaz genérica para la interacción con el usuario. Puede haber una oportunidad para dividir esta interfaz en interfaces más específicas, cada una responsable de una funcionalidad única para cumplir mejor con el SRP.
- **InfoUsuario**: Esta clase maneja la información general del usuario y se asocia con `InfoAccesoPersonal` a través de una relación compuesta, lo que implica que `InfoAccesoPersonal` es parte de `InfoUsuario`.
- **InfoAccesoPersonal**: Esta clase maneja la información de acceso personal del usuario, como nombre de usuario y contraseña. Forma parte de la clase `InfoUsuario`, lo que indica una relación de composición.
- **TarjetaDeCredito**: Representa una tarjeta de crédito y está asociada con `Cliente` mediante una relación de agregación, lo que indica que una tarjeta de crédito es parte de un cliente, pero también puede existir de forma independiente.
- **Cliente**: Esta clase se asocia con `InfoUsuario` mediante una relación simple, lo que sugiere que un cliente tiene una instancia de `InfoUsuario`. Además, se menciona que `Cliente` tiene una relación de agregación con `TarjetaDeCredito`, lo que implica que un cliente puede tener una o más tarjetas de crédito asociadas.

## Open/Closed Principle (OCP - Principio de Abierto/Cerrado):

- **InterfazUsuario**: Si separamos esta interfaz en interfaces más específicas, estaríamos cumpliendo mejor con el OCP al permitir que estas interfaces sean extendidas sin modificar el código existente.
- **Beneficios**: Esta clase abstracta parece ser un buen ejemplo de cómo aplicar el OCP. Puede ser extendida para proporcionar diferentes tipos de beneficios sin necesidad de modificar el código existente.

## Liskov Substitution Principle (LSP - Principio de Sustitución de Liskov):

- se cumple en este diagrama de clases, ya que no hay evidencia de que las subclases alteren el comportamiento esperado de la superclase. Cada clase y subclase están definidas con atributos y métodos específicos, sin sobrescribir o cambiar la funcionalidad existente de manera que viole el LSP.

## Interface Segregation Principle (ISP - Principio de Segregación de Interfaces):

- La división de la interfaz de usuario en interfaces más específicas puede ayudar a cumplir con el ISP, asegurando que los clientes solo dependan de las interfaces que necesitan.

## Dependency Inversion Principle (DIP - Principio de Inversión de Dependencias):

-Definir interfaces o abstracciones: En lugar de depender de implementaciones concretas, debemos crear interfaces o abstracciones que representen las funcionalidades requeridas por los módulos de alto nivel. Estas interfaces actúan como contratos que especifican los métodos y propiedades necesarios.
-Implementar los módulos de nivel inferior: Los módulos de nivel inferior, que contienen la implementación concreta de las funcionalidades, deben implementar las interfaces definidas. Por ejemplo, en el diagrama, la clase 'TarjetaDeCredito' implementa la interfaz 'IInterfazTarjeta' en lugar de ser directamente referenciada por la clase 'Cliente'.
