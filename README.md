# Django-project
Desarrollo en Django, app web para conteo de imágenes por servidores.
Desarrollo web con PYTHON, HTML, CSS y JAVASCRIPT, una tabla que muestra columnas de :
SERVIDOR, 
CAMARA, 
MES (imagenes a procesar en operadores), 
MES (siguiente a procesar una vez caduque el primero ya refleja la información cargada a procesar) OTROS(meses a revisar sus cámaras por alguna falencia en el nombre del formato), 
VIDEOS(videos procesándose en los servidores que pasarán a ser imágenes en la columna del mes, y se irán acumulando), 
MULTAS(por servidor que se hayan hecho)

La información que brinda cada uno, es reflejada a través de una base de datos con PostgreSQL, que recibe los parámetros del paraContar.py, a través de DataFrames, este mismo es absorvido por servidor cuando se ejecuta el código en cada uno con contar.py desde el mismo código.
