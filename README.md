# Documentación Técnica del Servicio Web de Análisis de Mortalidad No Fetal en Colombia (2019)

## 1. Introducción

Este documento describe la arquitectura, el proceso de desarrollo y el despliegue del servicio web diseñado para analizar los datos de mortalidad no fetal en Colombia durante el año 2019. El objetivo principal de esta aplicación es proporcionar una plataforma interactiva para la visualización y el análisis de estos datos, facilitando la generación de reportes y la obtención de *insights* relevantes.

## 2. Descripción General del Proyecto

El servicio web se implementa como una aplicación Python utilizando el microframework Dash, lo que permite la creación de interfaces de usuario interactivas y personalizadas para la exploración de los datos. La aplicación se encuentra desplegada en la plataforma *Platform as a Service* (PaaS) de Google Cloud Run, lo que garantiza su escalabilidad y disponibilidad.

Los diferentes módulos de la aplicación cuentan con sus respectivos DOCSTRING para describir cada componente creado.

## 3. Arquitectura y Componentes Principales

La arquitectura del servicio web se basa en los siguientes componentes clave:

* **Aplicación Dash (Python 3.11):** El núcleo de la aplicación, responsable de la lógica de presentación, la interacción con el usuario y la generación de visualizaciones.
* **Google Cloud Run:** La plataforma de despliegue que gestiona la infraestructura subyacente, asegurando la ejecución y el escalado automático de la aplicación.
* **Google BigQuery:** El almacén de datos principal donde se encuentran los datos de mortalidad no fetal correspondientes al año 2019.
* **GitHub:** El sistema de control de versiones utilizado para la gestión del código fuente y la colaboración en el desarrollo.
* **Google Cloud Build:** El servicio de integración continua y entrega continua (CI/CD) encargado de automatizar el proceso de construcción y despliegue de nuevas versiones de la aplicación.

## 4. Proceso de Despliegue y CI/CD

El proceso de Integración Continua y Entrega Continua (CI/CD) se gestiona mediante Google Cloud Build. Cada vez que se realiza una modificación en el archivo `Dockerfile` de la rama principal (`main`) del repositorio de GitHub, Cloud Build automáticamente:

1.  Construye una nueva imagen del contenedor Docker.
2.  Despliega la nueva imagen en el servicio de Cloud Run, actualizando la versión de la aplicación en producción.

Este flujo de trabajo asegura que las actualizaciones del código se implementen de manera eficiente y automatizada.

## 5. Almacenamiento de Datos

Los datos primarios para el análisis de mortalidad no fetal en 2019 se encuentran almacenados en Google BigQuery. Además, se han incorporado datos complementarios en la misma plataforma:

* **Anexo 4:** Coordenadas geográficas de los departamentos de Colombia.
* **Anexo 5:** Categorías de edades utilizadas para la agregación y el análisis de los datos de mortalidad.

## 6. Tecnologías Utilizadas

* **Lenguaje de Programación:** Python 3.11
* **Microframework Web:** Dash (Python)
* **Plataforma PaaS:** Google Cloud Run
* **Almacenamiento de Datos:** Google BigQuery
* **Control de Versiones:** Git (GitHub)
* **CI/CD:** Google Cloud Build

## 7. Próximos Pasos

En las siguientes secciones de esta documentación, se detallarán aspectos específicos de la aplicación, como la arquitectura de la aplicación, la conexión a BigQuery, la implementación de las visualizaciones y las instrucciones para el uso del servicio web:

* ### [Arquitectura de la aplicación](docs/arquitectura.md)
* ### [Despliegue de la aplicación](docs/despliegue.md)
* ### [Descripción de las fuentes de datos](docs/fuente_datos.md)
* ### [Conclusiones](docs/conclusiones.md)