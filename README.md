# API - DATA_SERVER #

Descripcion: Esta api esta destinada a servir alarmas para ser usada por algun cliente y notificar o alarmar
en algun medio de mensajeria.

## Estructura de carpetas ##
* conf.d : Contiene archivos de configuracion, como los requeriments a instalar de python y configuraciones del server.-
* database : En esta carpeta contiene la base de datos que alamcenara los usuarios en sqlite3, ademas de un template de esta base.
Tambien tiene en un archivo JSON las alarmas que se serviran desde la API.-
* packages : En esta carpeta se encuentran los modulos de la api como la clase en que maneja la base de datos dbSqlite.py tambien
tenemos el modulo que formatea los datos de las alarmas formatDataJSON.py despues tenemos el modulo que valida los accesos a la api
tokenValidator.py.-
* routes : En esta carpeta encontraremos las rutas disponibles de la api
* Dockerfile : Dentro de este archivo tenemos la configuracion para levantar la api en un contenedor.
* tmp : En este path encontraremos 3 archivos que corresponden a los 3 niveles de alarmas [green, yellow, red]. Estos deberan ser cargados 
en este path de la siguiente forma hostname|server una alarma debajo de la otra. 
* setup.py : En este archivo encontramos la configuracion para levantar el contenedor
## Funcionamiento ##
* Dockerfile : Si decidimos ejecutar desde un contenedor solamente tenemos que ejecutar el archivo setup.py esto levantara el conetenedor de 
docker attacheando unidades que estan descriptas en el script. Son para la base de datos y la edicion de alarmas.
* Localmente : Si deseamos ejecutarlo localmente debemos instalar los requeriments de la carpeta de conf.d y luego levantar la api desde app.py
* Alarmas :  Tenemos tres niveles de alarmas [green, yellow, red] las alarmas deben ser cargadas en los archivos de tmp una debajo de otra. 
hostname|alarma sin espacios una debajo de la otra. estas alarmas pueden ser cargadas mediante un cron y scripts de bash. de esta forma podrias 
manejar el tiempo y que monitorear. Mediante la api podrias servir estos datos para poder enviar alertas desde algun cliente que consuma la api.