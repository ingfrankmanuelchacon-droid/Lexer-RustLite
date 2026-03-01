# ==========================================
# LENGUAJE L: Suma de identificadores (id + id)
# ENTRADA A ANALIZAR
tokens_entrada = ['id', '+', 'id']
# ==========================================

print("--- 1. ANALIZADOR LL (Descenso Recursivo) ---")


class AnalizadorLL:

    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def actual(self):
        return self.tokens[self.pos] if self.pos < len(self.tokens) else None

    def coincidir(self, esperado):
        if self.actual() == esperado:
            self.pos += 1
        else:
            raise SyntaxError(f"Error LL: Esperaba {esperado}")

    def analizar(self):
        self.E()
        if self.actual() is None:
            print("Resultado LL: ¡Análisis exitoso de arriba hacia abajo!")

    # Regla: E -> id E'
    def E(self):
        print("LL: Entrando a E -> id E'")
        self.coincidir('id')
        self.E_prima()

    # Regla: E' -> + id E' | nulo
    def E_prima(self):
        if self.actual() == '+':
            print("LL: Entrando a E' -> + id E'")
            self.coincidir('+')
            self.coincidir('id')
            self.E_prima()
        else:
            print("LL: Entrando a E' -> nulo (fin)")


parser_ll = AnalizadorLL(tokens_entrada)
parser_ll.analizar()

print("\n--- 2. ANALIZADOR LR (Shift-Reduce) ---")


class AnalizadorLR:

    def __init__(self, tokens):
        self.tokens = list(tokens)
        self.pila = []

    def analizar(self):
        while len(self.tokens) > 0 or len(self.pila) > 1:
            # Intentar reducir primero
            # Regla 1: E -> E + id
            if len(self.pila) >= 3 and self.pila[-3:] == ['E', '+', 'id']:
                self.pila[-3:] = ['E']
                print(f"LR: Reduce usando [E -> E + id]. Pila: {self.pila}")
                continue

            # Regla 2: E -> id
            if len(self.pila) >= 1 and self.pila[-1] == 'id':
                # Solo reducimos 'id' a 'E' si no es parte de un '+ id' (simplificación)
                if len(self.pila) < 2 or self.pila[-2] != '+':
                    self.pila[-1] = 'E'
                    print(f"LR: Reduce usando [E -> id]. Pila: {self.pila}")
                    continue

            # Si no puede reducir, hace Shift
            if len(self.tokens) > 0:
                token = self.tokens.pop(0)
                self.pila.append(token)
                print(f"LR: Shift de '{token}'. Pila: {self.pila}")
            else:
                break

        if self.pila == ['E']:
            print("Resultado LR: ¡Análisis exitoso de abajo hacia arriba!")
        else:
            print("Resultado LR: Error de sintaxis.")


parser_lr = AnalizadorLR(tokens_entrada)
parser_lr.analizar()
