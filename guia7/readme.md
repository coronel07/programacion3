# Trabajo Práctico No 7 - Uso de Context Managers en Python

## Objetivo
El objetivo de este trabajo práctico es aprender y aplicar el concepto de context managers en Python para gestionar recursos de manera eficiente y segura.

## Implementación del Context Manager y Funciones

### Context Manager
El context manager `gestionar_archivo` se encarga de gestionar la apertura y cierre de archivos de manera segura. Utiliza el decorador `@contextmanager` del módulo `contextlib` para crear un generador. Dentro de este generador, abre el archivo utilizando la función `open` con los parámetros recibidos. Utiliza una estructura `try...finally` para asegurarse de que el archivo siempre se cierre correctamente después de que se hayan realizado todas las operaciones necesarias.

### Funciones de Lectura y Escritura
- La función `leer_archivo` utiliza el context manager `gestionar_archivo` para abrir un archivo en modo lectura y luego imprime cada línea del archivo.
- La función `escribir_archivo` utiliza el context manager `gestionar_archivo` para abrir un archivo en modo escritura y escribir varias líneas de texto en él.

## Ejemplo de Uso
```python
# Escribir en un archivo
escribir_archivo('prueba.txt')

# Leer desde un archivo
leer_archivo('prueba.txt')
