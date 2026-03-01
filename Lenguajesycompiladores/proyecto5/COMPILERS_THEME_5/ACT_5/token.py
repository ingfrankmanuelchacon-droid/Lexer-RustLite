class Token:
    def __init__(self, tipo, valor, linea, columna):
        self.tipo = tipo
        self.valor = valor
        self.linea = linea
        self.columna = columna

    def __repr__(self):
        return f"Token({self.tipo}, {self.valor}, {self.linea}, {self.columna})"


# Tipos de token
TT_KEYWORD = "KEYWORD"
TT_IDENT = "IDENT"
TT_NUMBER = "NUMBER"
TT_OPERATOR = "OPERATOR"
TT_PAREN = "PAREN"
TT_SEMICOLON = "SEMICOLON"
TT_WHITESPACE = "WHITESPACE"
TT_STRING = "STRING"
TT_UNKNOWN = "UNKNOWN"
