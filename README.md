# Introduccion
<p style="text-align: justify;">Este programa fue diseñado e implementado para mejorar la gestión de inventario de un almacén de tenis que se vea perjudicado por la manipulación manual del almacenamiento del producto. Esta APP se diseñó con Visual Estudio Code, Cmder, Tkinter como entorno virtual, lenguaje de programación Python, como base de datos se utilizó el software DB Browser SQLite, para implementar una app de escritorio que cumpla las expectativas del cliente y se emplee de acuerdo a sus necesidades.</p>

# Objetivos
### General

<p style="text-align: justify;"> Desarrollar y poner en marcha un software de inventario que trabaje de manera eficiente y confiable para un almacén de tenis, con el objetivo de mejorar la gestión de inventario y aumentar la eficiencia operativa.</p>

####  Especifico

- Analizar las necesidades del almacén de tenis y establecer los requerimientos funcionales del software de inventario.  

- Evaluar y mejorar la arquitectura del software para garantizar un desempeño óptimo y una alta disponibilidad.  

- Identificar oportunidades de mejora continua en la funcionalidad del software de inventario para aumentar la eficiencia y reducir costos.  

- Realizar pruebas exhaustivas del software de inventario para asegurar su funcionamiento correcto y la calidad de los datos gestionados.

Identificación de requerimientos

## Requerimientos Funcionales

**R1**. Permitirá visualizar los productos que están disponibles, así mismo actualizar datos de ingreso de los mismos.  

**Condiciones anormales:  **
Mostrará la información de que existe una duplicidad de datos.
Los datos ingresados no se verán de forma completa en la tabla.

**Criterios de aceptación:  **
Los datos ingresados son correctos.

**R2**. Permite crear tabla en la base de datos.

**Condiciones anormales:**
La tabla en la base de datos no se ha creado.
La tabla en la base de datos ya existe.

**Criterios de aceptación:  **
La tabla en la base de datos se ha creado correctamente.

**R3**. Interfaz clara, sencilla y flexible para el usuario.

**Condiciones anormales:**
Es difícil de navegar.
No hay campos para hacer el ingresa más sencillo 

**Criterios de aceptación:**
Uso aceptable y esperado por el usuario.

**R4.** Permitirá modificar los datos ingresados.

**Condiciones anormales:** 
Mostrará la información de que existe duplicidad de datos.
Los datos seleccionados no se verán de forma completa en los campos de dato.
 
**Criterios aceptables:**
Los datos modificados son correctos.

## Requerimientos no Funcionales

**RNF.1** Software  
Sistema operativo Windows. 
  
**RNF.2** Accesibilidad  
Respuesta optima respecto a los requerimientos del usuario.  

**RNF.3** Sin Conexión  
Enfocado en tiempo, disponibilidad y planes alternativos sin conexión a internet.  

**RNF.4 ** Uso  
Eficiencia de los ingresos, modificaciones, guardados, eliminaciones y visualización de los datos.


# Inventario de Tennis

Este proyecto se realizo con las aplicaciones [cmder](http://https://cmder.app/ "cmder")
[Visual Studio Code](http://https://code.visualstudio.com/ "Visual Studio Code") ------  [DB Browser SQLite](https://sqlitebrowser.org/ "DB Browser SQL Lite")

## Lenguaje de Programacion
[Python](http://https://www.python.org/ "Python")

## Entorno virtual venv
[tkinter](http://https://docs.python.org/3/library/tkinter.html "tkinter")

## Instalación
### Paso 1
**1 forma**. Dar clic en code y luego en Download Zip
**2 forma**. abrir la carpeta con cmder y ejecutar

`Repositorio Git https://github.com/yohanmira1/inventario.git`

### Paso 2
- crear una base de datos con el nombre de ** inventario**
- Luego  crear la tabla con nombre **inventario**
- Luego crear los atributos en la base de datos tales como:  **codigo_teni, marca, cantidad, precio, talla** respectivamente

### Paso 3 
-abri la base de datos con [DB Browser SQLite](http://https://sqlitebrowser.org/ "DB Browser SQLite")

# Vista previa 

## Interface

[![interface.png](https://i.postimg.cc/K8rrLQJ0/interface.png)](https://postimg.cc/3kNvQjMG)

## Crear o eliminar base de datos desde la aplicación
[![Crear-base-de-datos.png](https://i.postimg.cc/VkVs7PGv/Crear-base-de-datos.png)](https://postimg.cc/FY0QR8QX)

## Tabla en base de datos
[![tabla-en-base-de-datos.png](https://i.postimg.cc/jd2GMwG6/tabla-en-base-de-datos.png)](https://postimg.cc/QHL4ttNV)

## Datos en la DB
[![datos-en-base-de-datos.png](https://i.postimg.cc/s2Y8Mphz/datos-en-base-de-datos.png)](https://postimg.cc/qt7QY6wD)
