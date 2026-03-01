from parser import Parser
from lexer import Lexer

def imprimir_ast(nodos, nivel=0):
    if not isinstance(nodos, list):
        nodos = [nodos]
    for nodo in nodos:
        print("  " * nivel + str(type(nodo).__name__))
        if hasattr(nodo, "ident"):
            print("  " * (nivel + 1) + f"ident: {nodo.ident}")
            imprimir_ast(nodo.expr, nivel + 2)
        elif hasattr(nodo, "expr") and not hasattr(nodo, "cond"):
            # PrintNode
            imprimir_ast(nodo.expr, nivel + 1)
        elif hasattr(nodo, "cond"):
            # IfNode
            imprimir_ast(nodo.cond, nivel + 1)
            print("  " * (nivel + 1) + "then:")
            imprimir_ast(nodo.then_stmt, nivel + 2)
            if nodo.else_stmt:
                print("  " * (nivel + 1) + "else:")
                imprimir_ast(nodo.else_stmt, nivel + 2)
        elif hasattr(nodo, "left") and hasattr(nodo, "op"):
            # BinOpNode
            imprimir_ast(nodo.left, nivel + 1)
            print("  " * (nivel + 1) + f"op: {nodo.op}")
            imprimir_ast(nodo.right, nivel + 1)
        elif hasattr(nodo, "value") and not hasattr(nodo, "name"):
            # NumberNode o StringNode
            if isinstance(nodo.value, int):
                print("  " * nivel + f"Number: {nodo.value}")
            else:
                print("  " * nivel + f'String: "{nodo.value}"')
        elif hasattr(nodo, "name"):
            print("  " * nivel + f"Ident: {nodo.name}")


def main():
    code = 'pront x = 5; if x > 3 prnt(x) else prnt("no")'

    lexer = Lexer()
    tokens, sugerencias_lex = lexer.get_tokens(code)

    print("=" * 50)
    print("TOKENS CORREGIDOS")
    print("=" * 50)
    for tok in tokens:
        print(tok)

    print("\n" + "=" * 50)
    print("SUGERENCIAS DEL ANALIZADOR LÉXICO")
    print("=" * 50)
    for sug in sugerencias_lex:
        print(sug)

    parser = Parser(tokens)
    try:
        ast = parser.parse()
        print("\n" + "=" * 50)
        print("ÁRBOL DE SINTAXIS ABSTRACTA (AST)")
        print("=" * 50)
        imprimir_ast(ast)

        print("\n" + "=" * 50)
        print("SUGERENCIAS SINTÁCTICAS")
        print("=" * 50)
        if parser.sugerencias_sintacticas:
            for sug in parser.sugerencias_sintacticas:
                print(sug)
        else:
            print("No se generaron sugerencias sintácticas (análisis exitoso).")
    except Exception as e:
        print("\nError durante el parsing:", e)
        if parser.sugerencias_sintacticas:
            print("\nSugerencias sintácticas generadas:")
            for sug in parser.sugerencias_sintacticas:
                print(sug)


if __name__ == "__main__":
    main()
