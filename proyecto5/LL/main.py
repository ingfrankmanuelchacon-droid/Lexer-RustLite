# --- ANALIZADOR LL (TOP-DOWN) ---
class AnalizadorLL:

    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def actual(self):
        return self.tokens[self.pos] if self.pos < len(self.tokens) else None

    def consumir(self, esperado):
        if self.actual() == esperado:
            print(f"Consumiendo: {esperado}")
            self.pos += 1
        else:
            raise SyntaxError(f"Se esperaba {esperado} pero se encontró {self.actual()}")

    def parse_if(self):
        # Esta es la lógica de tu imagen, pero funcional
        self.consumir('IF')
        self.consumir('LPAREN')
        self.expression()
        self.consumir('RPAREN')
        self.statement()
        print("¡Sentencia IF analizada con éxito!")

    def expression(self):
        print("  -> Analizando expresión interna...")
        self.consumir('VARIABLE')

    def statement(self):
        print("  -> Analizando cuerpo del IF...")
        self.consumir('PRINT')


# --- PRUEBA DEL ANALIZADOR ---
tokens_de_entrada = ['IF', 'LPAREN', 'VARIABLE', 'RPAREN', 'PRINT']
parser = AnalizadorLL(tokens_de_entrada)
parser.parse_if()

