# Microservicio de Transferencia de Archivos de Una Carpeta a Otra

## Descripción

El Microservicio de Transferencia de Archivos es una aplicación Python simple construida con Flask, diseñada para mover archivos de una carpeta a otra. Este microservicio proporciona una forma conveniente de automatizar el proceso de transferencia de archivos entre directorios.

## Importante
Para que te pueda funcionar, debes añadir 2 carpetas en tu escritorio.
- /File_IN
- /File_OUT

## Tabla de Contenidos

- [Requisitos Previos](#requisitos-previos)
- [Cómo Empezar](#cómo-empezar)
- [Uso](#uso)
- [Endpoints](#end-points)
- [Contribuir](#contribuir)
- [Licencia](#licencia)

## Requisitos Previos

Antes de comenzar, asegúrate de cumplir con los siguientes requisitos:

- Tener Python 3.x instalado.
- Tener la librería Flask instalada (puedes instalarla usando pip).
- Conocimientos básicos sobre APIs RESTful.

## Cómo Empezar

Para comenzar con el Microservicio de Transferencia de Archivos, sigue estos pasos:

1. Clona este repositorio en tu máquina local:

   ```bash
   git clone https://github.com/tu-nombre/move-file-wiht-python.git

2. Cambia al directorio del proyecto:
   ```bash
   cd move-file-wiht-python

3. Instala las dependencias necesarias:
   ```bash
   pip install -r requirements.txt

4. Ejecuta la aplicación Flask::
   ```bash
   python app.py

Con esto el microservicio debería estar funcionando localmente.

## Uso

Este microservicio expone una API RESTful que te permite mover archivos de una carpeta a otra. Puedes interactuar con él utilizando solicitudes HTTP.

## Endpoints

# GET/activar
  - Mueve un archivo desde el directorio fuente al directorio de destino.

  - Respuesta : Los Archivos se han pasado a la carpeta destino.

## Contribuir

¡Las contribuciones son bienvenidas! No dudes en enviar una pull request o abrir problemas para cualquier mejora o corrección de errores.

## Licencia

Este proyecto está licenciado bajo la Licencia MIT.


Este README proporciona una descripción del proyecto, los requisitos previos, instrucciones para comenzar, cómo utilizar el microservicio, información sobre los puntos finales de la API, instrucciones para contribuir y la licencia del proyecto. Asegúrate de personalizarlo según tus necesidades y agregar más detalles sobre el funcionamiento del microservicio si es necesario.
