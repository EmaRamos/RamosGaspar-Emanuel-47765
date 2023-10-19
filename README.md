# Transportadoras MH
## Objetivo
Este es el repositorio de una web de **e-commerce** desarrollada en el curso de Python dictado en la comisión 47765 de Coderhouse.
Esta web, aún en desarrollo, tiene por objetivo **ofrecer un sitio de venta de kennels para el transporte de mascotas por vía área**.
## Tecnologías Utilizadas
-	**Lenguaje de Programación**: Python
-	**Framework de Desarrollo**: Django
-	**Base de Datos**: SQLite
-	**Frontend**: HTML, CSS y JavaScript
-	**Herramientas de Versionamiento**: Git y GitHub
## Descripción
El proyecto se compone de **2 apps**: **Store** contiene el core del proyecto y **Accounts** contiene el manejo de usuarios. Además cuenta con una carpeta **media** que permite subir imágenes y un archivo **xlsx** que contiene los tests realizados.
## Super-Usuario
**Username**: admin
**Password**: admin
## Modelos
La app **Store** cuenta con los siguientes modelos:
- **Categories**: incluye las categorías de productos ofrecidas (de momento solo 1).
- **Products**: incluye los productos ofrecidos.
- **Orders**: incluye las órdenes realizadas por los clientes.

La app **Accounts** no cuenta con modelos definidos.
## Vistas
En la app **Store** trabaja principalmente con **vistas basadas en clases** haciendo uso del modelo **Products**. De esta forma, facilita el CRUD de los productos a la venta.
En cambio, **Accounts** trabaja con **formularios y vistas basadas en funciones** para llevar adelante el manejo de usuarios que incluye login, registro y logout.
## Demo
https://drive.google.com/file/d/1YqCk3owTiU1-MPOk7-wvEIIU8-W3lVl7/view?usp=share_link
