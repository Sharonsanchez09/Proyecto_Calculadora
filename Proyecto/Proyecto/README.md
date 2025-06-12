# Calculadora de Funciones con Serie de Taylor

Este proyecto implementa funciones matemáticas usando Python, utilizando el patrón MVC.

## Funciones Implementadas

- e^x
- sin(x)
- cos(x)
- arcsin(x)
- arccos(x)
- sinh(x)
- cosh(x)

## Requisitos

- Python
- Flask (para la aplicacion web)

## Ejecución

# Para terminal

Desde la **carpeta raíz del proyecto**, ejecutar el siguiente comando en la terminal:

```
python -m controller.main
```

Esto abrirá el menú interactivo en la consola para usar la calculadora.

## Para la aplicación web

Desde la **carpeta raíz del proyecto**, ejecutar el siguiente comando en la terminal:

```
python -m web.app
```

Esto iniciará el servidor Flask.
Luego abrir en el navegador y entrar a [http://127.0.0.1:5000](http://127.0.0.1:5000).

**Nota:**
Asegúrarse de tener Flask instalado (`pip install flask`)
