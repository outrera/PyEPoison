# PyEPoison
Implementación de módulos de python para potenciar las capacidades del motor de Entidad 3D a base de scripts

## Documentación
### *Para las funciones importadas desde E3d_format.py*
-----


### Funciones de sistema

 ARCH_A_VAR |  ɣ
------------ | -------------
Syntaxis: | Variable = ARCH_A_VAR("nombre del archivo.extensión")   
Descripción: | Toma un archivo y lo convierte en una variable   
Nota: | Sólo lee la primera línea del archivo

VAR_A_ARCH |  ɣ
------------ | -------------
Syntaxis: | Variable = VAR_A_ARCH(variable, "nombre del archivo de destino.extensión")
Descripción: | Toma una variable y la convierte en un archivo
Nota: | A diferencia de ARCH_A_VAR, esta función si puede escribir un archivo entero de varias líneas
-----
### Funciones para GameJolt
#### Nota: La mayoría de las funciones dependen de un parámetro en archivo_de_configuracion.py (usrdata)
LOGIN |  ɣ
------------ | -------------
Syntaxis: | LOGIN()
Descripción: | Esta función lee los archivos ya creados en entidad 3d para permitirle al usuario iniciar sesión en GameJolt
Depende de archivos: | No

DAR_TROFEO |  ɣ
------------ | -------------
Syntaxis: | DAR_TROFEO()
Descripción: | Da un trofeo, especificado por Entidad3D
Depende de archivos: | Sí, Trophy.ini (Ahí se especifica la ID del trofeo)

INICIAR_SESION |  ɣ
------------ | -------------
Syntaxis: | INICIAR_SESION()
Descripción: | Inicia una sesión de juego para el jugador alojado
Depende de archivos: | No

MANTENER_ACTIVO |  ɣ
------------ | -------------
Syntaxis: | MANTENER_ACTIVO()
Descripción: | Le indica al servidor de GameJolt que el jugador se encuentra en una partida de tu juego.
Depende de archivos: | No

MANTENER_SESION |  ɣ
------------ | -------------
Syntaxis: | MANTENER_SESION()
Descripción: | Le indica a GameJolt que el juego está abierto, pero pausado o en un menú

GUARDAR_PUNT_SERV |  ɣ
------------ | -------------
Syntaxis: GUARDAR_PUNT_SERV()
Descripción: Guarda la puntuación del jugador actual
Depende de archivos: Sí, Table.ini (el indice de la tabla), Extra_data.ini (informacion extra que quieras almacenar, no es visible en el sitio), score.ini (descripción de la puntuación), sort.ini (el valor de la puntuación, númerico o texto)

GUARDAR_PUNT_CL |  ɣ
------------ | -------------
Syntaxis: | GUARDAR_PUNT_CL("Nombre del jugador", "indice de la tabla", número de jugador)
Descripción: | Guarda la puntuación del jugador en modo huesped.
Depende de archivos: | Sí, Table.ini (el indice de la tabla), Extra_data.ini (informacion extra que quieras almacenar, no es visible en el sitio), score.ini (descripción de la puntuación), sort.ini (el valor de la puntuación, númerico o texto)
Nota: | el estilo a seguir de los archivos debe ser: Cnum_de_jugadorArchivo.ini por ejemplo: C1Extra_Data.ini

CONS_PUNT_MAX |  ɣ
------------ | -------------
Syntaxis: | CONS_PUNT_MAX()
Descripción: | Pide al servidor de GJ las puntuaciones máximas (Regresa una lista en formato json)
Depende de archivos: | No

CONS_DATA |  ɣ
------------ | -------------
Syntaxis: | CONS_DATA()
Descripción: | Le indica al servidor de GameJolt que el jugador se encuentra en una partida de tu juego.
Depende de archivos: | No
