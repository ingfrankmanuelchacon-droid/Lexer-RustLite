import ast


def visualizar_ast(codigo):
    # Generamos el árbol a partir del string de código
    arbol = ast.parse(codigo)

    print(f"Estructura del código: '{codigo}'")
    for nodo in ast.walk(arbol):
        # Imprimimos el tipo de nodo y sus campos
        print(f"Nodo encontrado: {type(nodo).__name__}")
        if isinstance(nodo, ast.Name):
            print(f"  -> Variable: {nodo.id}")
        elif isinstance(nodo, ast.Constant):
            print(f"  -> Valor: {nodo.value}")


# --- Ejecución del ejemplo ---
ejemplo_entrada = "resultado = x + 10"
visualizar_ast(ejemplo_entrada)

