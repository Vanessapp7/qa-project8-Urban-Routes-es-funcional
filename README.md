# qa-project8-Urban-Routes-es-funcional

## Urban Routes

**Vanessa Pineda Perez - Cohort 21, Sprint 8**

Google Chrome: Navegador web necesario para ejecutar las pruebas automatizadas.

---

## Descripción del Proyecto

Urban Routes es una aplicación de servicio de taxis desarrollada para Tripleten. Permite a los usuarios pedir un taxi de manera eficiente y personalizada. Este proyecto se centra en implementar y probar funcionalidades clave para garantizar una experiencia fluida.

---

## Tecnologías y Herramientas Utilizadas

- **Python**: Lenguaje de programación utilizado para las pruebas.
- **Selenium**: Herramienta de automatización para interactuar con la interfaz web.
- **Unittest**: Framework para estructurar y ejecutar las pruebas.
- **Git**: Sistema de control de versiones para administrar el código fuente.

---

## Instrucciones para Ejecutar las Pruebas

1. **Instalar dependencias**:
    - Asegúrate de tener instalado **Python 3.x**.
    - Instala Selenium ejecutando el siguiente comando en la terminal:
      ```sh
      pip install selenium
      ```

2. **Ejecutar las pruebas**:
    - Abre la terminal, navega al directorio raíz del proyecto y ejecuta:
      ```sh
      pytest qa-project8-Urban-Routes-es/tests.py
      ```

---

## Requisitos del Proyecto

Para considerar las pruebas exitosas, deben cumplirse los siguientes criterios:

1. **Pruebas Automatizadas**:
    - Configuración de direcciones.
    - Selección de tarifas.
    - Ingreso de información de pago.
    - Solicitudes adicionales (manta, pañuelos, helados).
    - Verificación de aparición del modal de búsqueda de taxi.
2. **Código limpio y bien estructurado**:
    - Uso de variables y funciones descriptivas.
    - Funciones deben comenzar con verbos.
3. **Interacciones clave cubiertas**:
    - Entradas.
    - Botones.
    - Modales dinámicos.
4. **Uso adecuado de funciones de espera**:
    - Utilizar WebDriverWait en lugar de pausas estáticas (`time.sleep`).
5. **Uso de localizadores diversos**:
    - Deben usarse al menos 4 tipos diferentes de localizadores: `By.ID`, `By.CLASS_NAME`, `By.XPATH`, `By.CSS_SELECTOR`.

---

## Casos de Prueba Automatizados

Las pruebas automatizadas abarcan los siguientes pasos clave en el proceso de pedir un taxi:

1. **Configurar la dirección**:
    - Establecer la dirección de recogida y destino.
2. **Seleccionar la tarifa Comfort**:
    - Elegir la tarifa Comfort para el servicio.
3. **Rellenar el número de teléfono**:
    - Ingresar el número de teléfono y el código de confirmación interceptado.
4. **Agregar una tarjeta de crédito**:
    - Rellenar los campos de la tarjeta y activar el botón 'link' cambiando el enfoque del campo CVV.
5. **Escribir un mensaje para el conductor**:
    - Enviar un mensaje personalizado al conductor.
6. **Pedir una manta y pañuelos**:
    - Seleccionar estos elementos adicionales desde los interruptores.
7. **Pedir 2 helados**:
    - Simular la adición de dos helados como servicio adicional.
8. **Verificar la aparición del modal**:
    - Validar que el modal para buscar un taxi aparezca correctamente.

---

## Ejemplo de Resultado Esperado

- Al ejecutar las pruebas automatizadas, el código debe validar lo siguiente:
  - Direcciones ingresadas correctamente.
  - Tarifas seleccionadas.
  - Información de la tarjeta agregada exitosamente.
  - Mensaje enviado correctamente.
  - Elementos adicionales solicitados.
  - Modal de búsqueda de taxi visible.

---

## Conclusión

Este proyecto refuerza la calidad del software automatizando pruebas clave para la aplicación Urban Routes. Gracias a estas pruebas:
- Se asegura una experiencia de usuario sin errores antes del despliegue.
- Se identifican áreas de mejora durante el desarrollo.
- Se implementan prácticas sólidas en automatización de pruebas.

El proyecto Urban Routes es una excelente contribución al desarrollo profesional en la industria del software.

