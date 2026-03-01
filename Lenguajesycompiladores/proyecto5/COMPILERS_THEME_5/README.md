# UnegScript Hybrid Programming Assistant

Este proyecto implementa un asistente de programación híbrido para un subconjunto de Python llamado **UnegScript**. El sistema combina técnicas tradicionales de compilación (análisis léxico con expresiones regulares y análisis sintáctico descendente recursivo) con inteligencia artificial basada en distancia de Levenshtein y simulación de LLM para corregir errores tipográficos y sugerir correcciones.

## Características

- **Lexer híbrido**: 
  - Reconoce tokens mediante expresiones regulares (keywords, identificadores, números, operadores, paréntesis, punto y coma, cadenas).
  - Si un token no coincide con ninguna regla (o es un identificador muy similar a una keyword), se calcula su similitud con las palabras clave usando la distancia de Levenshtein.
  - Si la confianza es ≥ 0.8, se corrige automáticamente; si es menor, se consulta una IA simulada.
- **Parser descendente recursivo con lookahead**:
  - Construye un AST (Abstract Syntax Tree) para representar la estructura del programa.
  - Si encuentra un error de sintaxis, consulta a la IA (simulada) para obtener una sugerencia de corrección.
- **Ejemplo de procesamiento**:
  - Entrada: `pront x = 5; if x > 3 prnt(x) else prnt("no")`
  - Salida: tokens corregidos, sugerencias léxicas, y (si es posible) el AST.

## Estructura de ACT_5
```bash
├── token.py # Definición de Token y constantes
├── levenshtein.py # Funciones de distancia y confianza
├── lexer.py # Analizador léxico híbrido
├── ast_nodes.py # Clases de nodos del AST
├── parser.py # Analizador sintáctico
├── main.py # Punto de entrada
└── README.md # Documentación
```


## Requisitos

- Python 3.6 o superior.
- No requiere librerías externas (usa solo `re` del estándar).

## Ejecución

1. Clona o descarga los archivos en una misma carpeta.
2. Abre una terminal en esa carpeta.
3. Ejecuta:
   ```bash
   python main.py
   ```