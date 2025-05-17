# Proceso de Despliegue de la Aplicación

El despliegue de la aplicación web de análisis de mortalidad no fetal se realiza de manera automatizada mediante Google Cloud Build, siguiendo un proceso de Integración Continua y Entrega Continua (CI/CD). A continuación, se describen los pasos principales involucrados:

## 1. Configuración de la Integración con GitHub y Cloud Build

* **Enlace del Repositorio:** Se establece una conexión entre el repositorio de GitHub que contiene el código fuente de la aplicación y el servicio Google Cloud Build. Esta configuración permite a Cloud Build monitorear los cambios en el repositorio y activar automáticamente los procesos de construcción y despliegue. Los detalles específicos de esta configuración se pueden encontrar en la documentación oficial de Google Cloud: [Despliegue continuo con Cloud Build](https://cloud.google.com/run/docs/continuous-deployment-with-cloud-build#new-service)
    * Es importante destacar que la documentación oficial proporciona una guía paso a paso para configurar la conexión entre GitHub y Cloud Build, incluyendo la autenticación y la definición de los eventos que dispararán las construcciones.

## 2. Configuración del Servicio en Cloud Run

Se configura el servicio en Google Cloud Run para alojar la aplicación contenerizada. Esta configuración incluye los siguientes aspectos clave:

* **Número Máximo de Instancias:** Se establece un límite máximo de 2 nodos para el autoescalamiento del servicio. Esto permite a Cloud Run escalar automáticamente el número de instancias de la aplicación en función de la demanda, hasta un máximo de 2 instancias simultáneas.
* **Autoescalamiento:** Se habilita el autoescalamiento para el servicio de Cloud Run. Esto significa que Cloud Run ajustará dinámicamente el número de instancias en ejecución para manejar las variaciones en el tráfico, optimizando el rendimiento y los costos.
* **Deshabilitación de Autenticación de IAM:** Se configura el servicio para que no requiera autenticación de Identity and Access Management (IAM). Esto significa que la aplicación será accesible públicamente a cualquier persona que conozca la URL.  *Nota importante: Esta configuración debe revisarse cuidadosamente en un entorno de producción para garantizar la seguridad adecuada. Se recomienda habilitar la autenticación de IAM y configurar los permisos necesarios para controlar el acceso a la aplicación.*
* **Exposición Segura (HTTPS):** Se configura el servicio para que se exponga a través de una conexión segura HTTPS en la URL asignada por Cloud Run: `https://act4-unid2-app1-998899473084.us-central1.run.app`. Esto garantiza que la comunicación entre los usuarios y la aplicación esté cifrada y protegida.
* **Enlace con el Trigger de Cloud Build:** Se vincula el servicio de Cloud Run con el trigger de Cloud Build configurado previamente. Esto asegura que cada vez que Cloud Build detecte un cambio en el repositorio de GitHub (según la configuración del trigger), se active un nuevo despliegue de la aplicación en Cloud Run.

## 3. Despliegue Inicial

* **Dockerfile Inicial:** El primer despliegue de la aplicación se realiza utilizando la primera versión del archivo `Dockerfile` que se encuentra en la rama principal (`main`) del repositorio de GitHub. El `Dockerfile` contiene las instrucciones para construir la imagen del contenedor Docker que se ejecutará en Cloud Run.
* **Imagen del Contenedor:** Cloud Build utiliza el `Dockerfile` para construir una imagen de contenedor que incluye el código de la aplicación, sus dependencias y el entorno de ejecución necesario.
* **Despliegue en Cloud Run:** Cloud Build despliega la imagen del contenedor resultante en el servicio de Cloud Run, creando así la primera versión en ejecución de la aplicación.

## 4. Verificación del Despliegue

* **Inicio del Servicio Web:** Se verifica que la aplicación inicie correctamente el servicio web de Gunicorn. Gunicorn es un servidor WSGI (Web Server Gateway Interface) que permite ejecutar aplicaciones web Python, como la aplicación Dash, en un entorno de producción.
* **Acceso a la Aplicación:** Se verifica que la aplicación Dash esté accesible a través de la URL asignada por Cloud Run (`https://act4-unid2-app1-998899473084.us-central1.run.app`). Esto confirma que el despliegue se ha realizado correctamente y que los usuarios pueden acceder a la aplicación a través de la web.

Este proceso automatizado garantiza que las nuevas versiones de la aplicación se desplieguen de manera rápida, eficiente y confiable, reduciendo el riesgo de errores humanos y asegurando la disponibilidad continua del servicio.
