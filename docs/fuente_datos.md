# Fuentes de Datos

## Fuentes de Datos Iniciales

Los datos iniciales para el análisis de mortalidad no fetal se almacenaron en las siguientes tablas de Google BigQuery, dentro del dataset `trusty-equinox-459916-c5.Act3_data`:

* `anexo1_no_fetal`: Contiene los datos primarios de mortalidad no fetal.
* `anexo2_cods_muerte`: Almacena los códigos de las causas de muerte.
* `anexo3_divi_pola`: Incluye la división político-administrativa de Colombia.

## Fuentes de Datos Adicionales

Además de las fuentes de datos iniciales, se incorporaron las siguientes tablas adicionales para enriquecer el análisis:

* `anexo4_geo_info_dept`: Esta tabla contiene información geográfica relevante para el análisis espacial de la mortalidad, específicamente la latitud y longitud de cada departamento de Colombia.
* `anexo5_rango_edades`: Esta tabla proporciona la información completa sobre los rangos de edades utilizados para la clasificación y el análisis de los datos de mortalidad por grupos de edad.
