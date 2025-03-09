# qa-project8-Urban-Routes-es

# Urban Routes

**Vanessa Pineda Perez - Cohort 21, Sprint 8**

Google Chrome: Navegador web para ejecutar las pruebas.

---

## Descripción del Proyecto

Urban Routes es una aplicación de servicio de taxis en Tripleten que permite a los usuarios pedir un taxi de manera rápida y eficiente.
Este proyecto se enfoca en implementar y probar varias funcionalidades clave de la aplicación, asegurando que el proceso de pedir un taxi sea fluido y sin problemas.

---

## Tecnologías y Técnicas Utilizadas

- **Python**: Lenguaje de programación utilizado para escribir las pruebas automatizadas.
- **Selenium**: Herramienta de automatización utilizada para interactuar con la aplicación web y realizar las pruebas.
- **Unittest**: Framework de pruebas utilizado para estructurar y ejecutar las pruebas automatizadas.
- **Git**: Sistema de control de versiones utilizado para gestionar el código fuente del proyecto.

---

## Instrucciones para Ejecutar las Pruebas

1. Asegúrate de tener instaladas las siguientes herramientas y bibliotecas:
    - **Python 3.x**
    - **Selenium**: Podemos instalarlo con el siguiente comando:
      ```sh
      pip install selenium
      ```
2. Ejecutar el archivo principal de pruebas automatizadas con el siguiente comando:
   ```sh
   pytest ruta/del/proyecto/tests.py

Requisitos del Proyecto

-Pruebas escritas para todos los escenarios clave.

-Código bien formateado y fácil de leer.

-Uso de al menos 4 tipos de localizadores distintos.

Las pruebas interactúan con las entradas.

Sí, el código interactúa con entradas como las direcciones de origen
y destino usando set_from y set_to.

Las pruebas interactúan con los botones.

Tu prueba principal no lo hace aún, pero versiones extendidas de tu código cubren interacciones
con botones (por ejemplo, seleccionar tarifas o enviar formularios). Agregar pruebas específicas
para botones garantizará que este criterio esté cubierto.

Las funciones de espera se utilizan correctamente.

Sí, se utiliza WebDriverWait en varias partes del código para garantizar que los elementos estén
disponibles antes de interactuar con ellos.

-Interacción con:

    Entradas
    Botones
    Modales dinámicos
    Funciones de espera implementadas correctamente.
    Variables y funciones con nombres descriptivos.

Ejemplo: Las funciones deben comenzar con verbos.
         Evitar abreviaturas inapropiadas.
         Casos de Prueba Automatizados

✔️ Configurar la dirección ✔️ Seleccionar la tarifa Comfort ✔️ Rellenar el número de
teléfono ✔️ Agregar una tarjeta de crédito ✔️ Escribir un mensaje para el conductor
✔️ Pedir una manta y pañuelos ✔️ Pedir 2 helados ✔️ Verificar la aparición del modal
para buscar un taxi ✔️ Esperar la información del conductor en el modal (opcional)

Pre-requisitos

Asegúrate de tener instaladas las siguientes herramientas y bibliotecas:
Python 3.x
Selenium: Podemos instalarlo con el siguiente comando: pip install selenium

Conclusiones
En conclusión, el proyecto Urban Routes no solo ha cumplido con sus objetivos técnicos,
sino que también ha proporcionado un valioso aprendizaje en cuanto a la implementación y
prueba de aplicaciones web. Gracias a las pruebas automatizadas:
Se ha fortalecido la calidad del software.
Se han identificado áreas de mejora antes de desplegar la aplicación.
Este proyecto es un excelente paso hacia el desarrollo profesional
en la industria de software.

Descripción de las Pruebas Automatizadas para Pedir un Taxi (Sprint 8)

*Configurar la dirección: Establecer la dirección de recogida y destino.
*Seleccionar la tarifa Comfort: Elegir la tarifa Comfort para el servicio de taxi.
*Rellenar el número de teléfono: Ingresar el número de teléfono del usuario.
*Agregar una tarjeta de crédito: Ingresar los detalles de la tarjeta de crédito y
cambiar el enfoque del campo CVV para activar el botón 'link'.
*Escribir un mensaje para el conductor: Enviar un mensaje al conductor con instrucciones
o solicitudes adicionales.
*Pedir una manta y pañuelos: Solicitar una manta y pañuelos como elementos adicionales.
*Pedir 2 helados: Pedir dos helados como parte del servicio.
*Esperar a que aparezca la información del conductor (opcional): Verificar que la
información del conductor aparezca en el modal de búsqueda de conductor.

Automatización de Pruebas
Hemos desarrollado un conjunto de pruebas automatizadas utilizando Selenium y Unittest,
que cubren el proceso completo de pedir un taxi. Estas pruebas aseguran que las
funcionalidades clave de la aplicación, como:
-Configuración de direcciones.
-Selección de tarifas.
-Ingreso de información de pago.
-Solicitudes adicionales.
