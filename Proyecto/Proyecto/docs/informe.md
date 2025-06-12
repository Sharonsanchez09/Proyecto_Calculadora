# Informe del Proyecto: Calculadora Matemática con Series de Taylor

## 1. Análisis

En este proyecto se desarrollo una calculadora matemática que puede aproximar funciones como exponencial, seno, coseno, sus inversas y funciones hiperbólicas, usando solo series de Taylor.  
La idea era que la calculadora funcionara tanto en la terminal como en una página web, para que el usuario pudiera elegir la función y el valor que quisiera calcular.

### Requerimientos principales

- Aproximar funciones matemáticas sin usar librerías externas o funciones nativas de python.
- Tener una interfaz en la terminal y otra en la web.
- Validar bien lo que el usuario ingresa.
- Que el código sea modular y fácil de entender.

---

## 2. Diseño

### Estructura de carpetas

```
Proyecto/
│
├─ model/         # Aquí va la lógica matemática (series de Taylor)
├─ view/          # Interfaz para la terminal
├─ controller/    # Controlador de la aplicación
├─ web/           # Interfaz web con Flask
├─ docs/          # Documentación del proyecto
```

### Componentes principales

- **model/funciones.py:** Aquí están todas las funciones matemáticas hechas con series de Taylor.
- **view/terminal.py:** Es el menú interactivo para la terminal, donde se valida lo que el usuario ingresa y se muestran los resultados.
- **controller/main.py:** Es el archivo principal para arrancar la app en la terminal.
- **web/app.py:** Es la aplicación web hecha con Flask, donde hay un formulario para elegir la función y el valor.
- **web/static/styles.css:** Son los estilos para que la web se vea mejor.

---

## 3. Codificación

### model/funciones.py

- Aquí se programaron las funciones como `exp`, `sin`, `cos`, `arcsin`, `arccos`, `sinh`, `cosh` y `pi` usando solo operaciones básicas y ciclos.
- No se usaron librerías externas como `math`.

### view/terminal.py

- El menú es claro y fácil de usar.
- Permite elegir la función y el valor de entrada.
- Muestra cuál opción se eligió y el resultado.
- Valida que lo que se ingresa sea correcto y esté en el rango.

### controller/main.py

- Solo llama a la función principal del menú de la terminal.

### web/app.py

- Usa Flask para mostrar un formulario web.
- Permite elegir la función y el valor de entrada.
- Muestra el resultado en la misma página.
- Usa CSS para que la web se vea más bonita.

---

## 4. Conclusiones

El proyecto cumple con el objetivo de aproximar funciones matemáticas usando series de Taylor, y tiene una interfaz amigable tanto en la terminal como en la web.  
La estructura modular hace que sea fácil de mantener y ampliar.
