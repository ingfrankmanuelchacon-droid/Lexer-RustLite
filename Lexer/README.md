# Analizador Léxico para RustLite (Lenguaje L)

Este repositorio contiene un Lexer (Analizador Léxico) desarrollado con el metacompilador **ANTLR4** y ejecutado sobre **Python 3**. El objetivo es reconocer un subconjunto de la sintaxis del lenguaje Rust.

## 🛠️ Requisitos e Instalación

Para ejecutar este proyecto, necesitas tener instalado Python 3 y el entorno de ANTLR4.

1. **Instalar el runtime de ANTLR4 para Python:**

   ```bash
   pip install antlr4-python3-runtime
   🛠️ Instalación y Configuración
   Sigue estos pasos para preparar tu entorno de desarrollo:

   ```

1. **Dependencias de Python**
   Instala el motor de ejecución de ANTLR y las herramientas de generación:

**pip install antlr4-python3-runtime antlr4-tools** 2. Generar el Lexer (Metacompilación)
Si realizas cambios en las reglas de RustLite.g4, debes regenerar el analizador con este comando:

**antlr4 -Dlanguage=Python3 RustLite.g4** 3. Ejecutar el Análisis
Para procesar el código de prueba y ver la tabla de tokens:

**python main.py**

```
📁 Estructura del Proyecto
📄 RustLite.g4	Gramática oficial: Contiene las reglas léxicas y expresiones regulares.
🐍 main.py	Controlador: Punto de entrada que carga el código y ejecuta el Lexer.
⚙️ RustLite.py	Código Generado: El lexer en Python creado por ANTLR (no editar).
🚫 .gitignore	Filtro: Evita subir archivos temporales y basura al repositorio.
```
