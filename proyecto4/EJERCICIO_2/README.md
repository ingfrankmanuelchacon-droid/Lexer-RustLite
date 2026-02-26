```
INSTRUCCIONES
2) Construya un lexer para la verificación de archivos docker mediante expresiones regulares.

En el Informe debe indicar paso a paso la construcción de su lexer y 3 ejemplos de
ejecución.

En el archivo comprimido entregar los código (fuentes y ejecutables).
```

# Analizador Léxico para Dockerfiles (Lexer)

Este proyecto consiste en el desarrollo de un **Lexer** diseñado para identificar y clasificar los componentes léxicos (tokens) dentro de un archivo de configuración de Docker (Dockerfile). El análisis se realiza mediante el uso de expresiones regulares en Python.

## 📁 Estructura del Proyecto

* **lexer_docker.py**: Contiene la lógica principal de la clase `DockerLexer` y la definición de las expresiones regulares.
* **main.py**: Script de ejecución que contiene los casos de prueba y la lógica para mostrar los resultados en consola de forma tabular.
* **README.md**: Documentación del proyecto.

## 🛠️ Requisitos

* **Python 3.x**
* No se requieren librerías externas adicionales (se utiliza la librería estándar `re`).

## 🚀 Instalación y Ejecución

Para ejecutar el analizador y visualizar los ejemplos de ejecución, siga estos pasos:

1.  **Activar el entorno virtual:**
    En PowerShell:
    ```powershell
    .\.venv\Scripts\activate
    ```
    *(En caso de error de permisos, asegúrese de haber ejecutado la política de ejecución correspondiente).*

2.  **Ejecutar el script principal:**
    ```bash
    python main.py
    ```

## 🔍 Funcionamiento Técnico

El lexer procesa el texto identificando las siguientes categorías de tokens mediante expresiones regulares:
* **INSTRUCTION**: Comandos nativos de Docker (`FROM`, `RUN`, `COPY`, etc.).
* **COMMENT**: Líneas de documentación iniciadas con `#`.
* **ARGUMENT**: Parámetros y valores asociados a cada instrucción capturados mediante *lookbehind*.

La implementación utiliza el método `re.finditer` para realizar un análisis eficiente sobre el código fuente.

## 📝 Casos de Prueba Incluidos
El archivo `main.py` ejecuta automáticamente tres escenarios representativos:
1. **Configuración Básica**: Validación de flujo estándar.
2. **Variables y Comentarios**: Validación de metadatos y documentación.
3. **Multi-stage Build**: Validación de sintaxis compleja y alias.