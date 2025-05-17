# Arquitectura de la Aplicación Web de Análisis de Mortalidad No Fetal

## 1. Acceso a la Aplicación

Los usuarios pueden acceder al servicio web a través de la siguiente URL:
```
https://act4-unid2-app1-998899473084.us-central1.run.app
```
Esta URL dirige al servicio desplegado en Google Cloud Run.

## 2. Entorno de Despliegue en Google Cloud

El proyecto se encuentra alojado en la infraestructura de Google Cloud, bajo el siguiente ID de proyecto:
```
trusty-equinox-459916-c5
```

Todos los recursos y servicios utilizados por la aplicación se gestionan dentro de este proyecto de Google Cloud.

## 3. Microframework Dash (Python)

La interfaz de usuario y la lógica de presentación de la aplicación se construyen utilizando Dash, un microframework de Python diseñado específicamente para la creación de aplicaciones web interactivas para la visualización de datos.

* **Callbacks**: Dash se basa en un sistema de *callbacks* que permite la interacción dinámica entre los componentes del frontend (elementos de la interfaz de usuario) y el backend (la lógica de procesamiento de datos en Python). Cuando un usuario interactúa con un elemento en la interfaz (por ejemplo, selecciona un filtro o hace clic en un botón), se activa un *callback* que ejecuta código Python en el servidor y actualiza los componentes relevantes en la interfaz de usuario sin necesidad de recargar la página completa.
* **Backend y Frontend Integrados**: Dash facilita el desarrollo de aplicaciones web completas en Python, integrando tanto la lógica del servidor como la generación de la interfaz de usuario en un único flujo de trabajo de desarrollo.

## 4. Despliegue en Google Cloud Run

La aplicación desarrollada con Dash se encuentra desplegada en Google Cloud Run, un servicio de computación sin servidores que permite ejecutar contenedores Docker de forma escalable y gestionada.

* **Infraestructura Gestionada**: Cloud Run abstrae la complejidad de la gestión de la infraestructura subyacente (servidores, redes, etc.), permitiendo al equipo de desarrollo centrarse en la lógica de la aplicación.
* **Escalabilidad Automática**: Cloud Run escala automáticamente el número de instancias de la aplicación en función del tráfico y la demanda, garantizando un rendimiento óptimo incluso en momentos de alta concurrencia.

## 5. Almacenamiento de Datos en BigQuery

Los datos utilizados para generar los diferentes reportes y visualizaciones en la aplicación de Dash se encuentran almacenados en Google BigQuery, un almacén de datos empresarial completamente gestionado y sin servidores que permite realizar consultas SQL rápidas y a gran escala.

* **Dataset**: Los datos relevantes para esta aplicación se encuentran dentro del dataset denominado:

    ```
    trusty-equinox-459916-c5.Act3_data
    ```

* **Eficiencia en el Análisis**: BigQuery proporciona la capacidad de procesar grandes volúmenes de datos de manera eficiente, lo que es crucial para la generación de los análisis y reportes presentados en la aplicación Dash.

## 6. Integración Continua y Entrega Continua (CI/CD) con Cloud Build

El proceso de CI/CD para la aplicación se gestiona mediante Google Cloud Build, un servicio completamente gestionado que permite automatizar la construcción, prueba y despliegue de aplicaciones.

* **Automatización del Despliegue**: Cloud Build monitorea los cambios en el repositorio de código fuente (GitHub) y, según la configuración definida (en este caso, cualquier modificación en el archivo `Dockerfile` de la rama `main`), automáticamente construye una nueva imagen del contenedor y la despliega en Cloud Run.
* **Garantía de la Versión en Producción**: Este proceso automatizado asegura que la versión de la aplicación desplegada en producción siempre refleje los últimos cambios aprobados en el código fuente.

## 7. Seguridad de la Aplicación con Cloud IAM

La seguridad y el control de acceso a la aplicación y sus recursos en Google Cloud se gestionan mediante Cloud Identity and Access Management (IAM).

* **Control de Acceso Granular**: Cloud IAM permite definir y aplicar políticas de acceso detalladas, especificando qué usuarios o servicios tienen permisos para realizar qué acciones sobre los recursos del proyecto (por ejemplo, acceder a BigQuery, gestionar Cloud Run, etc.).
* **Seguridad Centralizada**: La gestión centralizada de la seguridad a través de Cloud IAM facilita la administración de los permisos y garantiza que solo las entidades autorizadas puedan interactuar con la aplicación y sus datos.
