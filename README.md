# Inventario Con Base de Datos que hace Crud que cuenta con una  interfaz grafica (GUI).

## Descripción.

Este programa se basa en la creacion y edicion de tablas de datos que contienen datos del inventario ya sea de un producto, un aula de clases, entre otras. 

## Objetivivo del codigo. 

El principal objetivo de codigo, es tener un a interfaz grafica para que eusurio ingrese los datos y puedan ser guardados en un base de datos en este codio se uso sqlite3, y ademas, de ingresar tambien pueda eliminar y editar estos datos.

## Notas. 
este progrma esta en su fase beta y se puede mejorar y optimizar como de igual manera agregar funciones.

# Recurso del codigo.

Para la realizacion del codigo se uso:
* El lenguaje de programación PYTHON
    * creacion de entornos virtuales.
    * Se agrego liberia de pip la cuales pueden verificar en el codigo.
    * libreia de tkinder para interfaz grafíca y su funcionabilidad
* el lenguaje de base de datos SQLITE3
    *Dprograma DB-BROWSER para navegar por la base de datos 
* Archivo .ico para el icono del GUI

# Estructura del codigo.

Este codigo se dividio en diferentes archivo para hacerlo mas comodo y se visualize mejor el funcionamiento y estan estructurado de la siguente manera 

* archivo inventario.py seria el principal que ejecuta todo el frame de la interfaz grafiaca
* carpeta Client que contine archivo gui_app.py que son todos los parametros y fuinciones de la interfaz grafíca
* Carpeta Database la cual contiene el archivo inventario.db que es la base de datos
* carpeta img aqui esta el archivo .ico el cual es el icono del programa
* La carpeta Model la cual esta el archivo conexion_db.py el cual nos enlaza la base de datos sqlite3 para poder creala y modificarla, y tambien se encuentra el archivo inventario_db.py el cual le da las funciones y paramatreos de la base de datos al Gui y contine el lenguaje sqlite para establecer pararamertro y funciones de nuestar base de datos y lenguaje python para dar la funciuonabilidad a la Gui. 

# Roadmap de Codigo.

Las funcionabilidades actuales de programa 

* [x] Crear y eliminar tabla de datos
* [x] Agregar Campos y/o datos a la tabla 
* [x] Funciones de botones Agregar, Guardar, Cancelar, Editar, y eliminar
* [x] Mostar tabla en pantalla actualizada 
  





