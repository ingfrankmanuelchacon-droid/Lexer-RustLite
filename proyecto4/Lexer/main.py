import sys
from antlr4 import *
from RustLite import RustLite  # 


def main():

    codigo_fuente = """
    fn main() {
        let mut x: i32 = 10;
        let y: i32 = x + 5;
        //Mira que estamos haciendo
        return y;
    }
    """
    
    print("--- Iniciando Análisis Léxico ---")
    print(f"Código fuente:\n{codigo_fuente}\n")

    # 1. Convertir el texto a un flujo de caracteres
    input_stream = InputStream(codigo_fuente)
    
    # 2. Inicializar el Lexer con ese flujo
    lexer = RustLite(input_stream)
    
    # 3. Obtener todos los tokens
    token_stream = CommonTokenStream(lexer)
    token_stream.fill()  # Forzar la carga de todos los tokens

    # 4. Imprimir los tokens encontrados
    print(f"{'TYPE':<15} {'TEXT':<10}")
    print("-" * 30)
    
    # Lista de nombres de reglas para que se vea bonito
    rule_names = lexer.ruleNames

    for token in token_stream.tokens:
        if token.type == -1:  # EOF (Fin de archivo)
            break
            
        nombre_token = rule_names[token.type - 1]
        texto_token = token.text.replace('\n', '\\n')
        
        print(f"{nombre_token:<15} '{texto_token}'")


if __name__ == '__main__':
    main()
