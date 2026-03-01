from token import (
    TT_KEYWORD,
    TT_IDENT,
    TT_NUMBER,
    TT_OPERATOR,
    TT_PAREN,
    TT_SEMICOLON,
    TT_STRING,
)
from ast_nodes import (
    AssignNode,
    PrintNode,
    IfNode,
    BinOpNode,
    NumberNode,
    IdentNode,
    StringNode,
)


class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0
        self.current_token = self.tokens[self.pos] if tokens else None
        self.sugerencias_sintacticas = []

    def next_token(self):
        self.pos += 1
        if self.pos < len(self.tokens):
            self.current_token = self.tokens[self.pos]
        else:
            self.current_token = None

    def lookahead(self):
        if self.pos + 1 < len(self.tokens):
            return self.tokens[self.pos + 1]
        return None

    def error(self, mensaje, token_actual, esperados):
        sugerencia = self._consultar_ia_sintactica(token_actual, esperados)
        self.sugerencias_sintacticas.append(
            f"Error en línea {token_actual.linea}: {mensaje}. {sugerencia}"
        )
        raise Exception(f"Error de sintaxis: {mensaje}")

    def _consultar_ia_sintactica(self, token, esperados):
        if token.tipo == TT_IDENT and token.valor == "prnt" and TT_KEYWORD in esperados:
            return "Sugerencia: cambiar 'prnt' por 'print'."
        return "No se pudo determinar una corrección automática."

    def parse(self):
        return self.programa()

    def programa(self):
        nodos = []
        while self.current_token is not None:
            stmt = self.sentencia()
            nodos.append(stmt)
            if self.current_token and self.current_token.tipo == TT_SEMICOLON:
                self.next_token()
            else:
                if self.current_token is not None:
                    self.error("Se esperaba ';'", self.current_token, [TT_SEMICOLON])
        return nodos

    def sentencia(self):
        tok = self.current_token
        if tok.tipo == TT_IDENT:
            if (
                self.lookahead()
                and self.lookahead().tipo == TT_OPERATOR
                and self.lookahead().valor == "="
            ):
                return self.asignacion()
            else:
                self.error(
                    "Se esperaba asignación o sentencia válida",
                    tok,
                    ["=", "print", "if"],
                )
        elif tok.tipo == TT_KEYWORD and tok.valor == "print":
            return self.print_sentencia()
        elif tok.tipo == TT_KEYWORD and tok.valor == "if":
            return self.if_sentencia()
        else:
            self.error("Sentencia no reconocida", tok, ["identificador", "print", "if"])
            return None

    def asignacion(self):
        ident = self.current_token
        self.next_token()
        if self.current_token.tipo != TT_OPERATOR or self.current_token.valor != "=":
            self.error("Se esperaba '='", self.current_token, ["="])
        self.next_token()
        expr = self.expresion()
        return AssignNode(ident.valor, expr)

    def print_sentencia(self):
        self.next_token()
        if self.current_token.tipo != TT_PAREN or self.current_token.valor != "(":
            self.error("Se esperaba '(' después de print", self.current_token, ["("])
        self.next_token()
        expr = self.expresion()
        if self.current_token.tipo != TT_PAREN or self.current_token.valor != ")":
            self.error(
                "Se esperaba ')' después de la expresión", self.current_token, [")"]
            )
        self.next_token()
        return PrintNode(expr)

    def if_sentencia(self):
        self.next_token()
        cond = self.expresion()
        then_stmt = self.sentencia()
        else_stmt = None
        if (
            self.current_token
            and self.current_token.tipo == TT_KEYWORD
            and self.current_token.valor == "else"
        ):
            self.next_token()
            else_stmt = self.sentencia()
        return IfNode(cond, then_stmt, else_stmt)

    def expresion(self):
        left = self.termino()
        while (
            self.current_token
            and self.current_token.tipo == TT_OPERATOR
            and self.current_token.valor in (">", "<", "=")
        ):
            op = self.current_token.valor
            self.next_token()
            right = self.termino()
            left = BinOpNode(left, op, right)
        return left

    def termino(self):
        tok = self.current_token
        if tok.tipo == TT_NUMBER:
            self.next_token()
            return NumberNode(int(tok.valor))
        elif tok.tipo == TT_IDENT:
            self.next_token()
            return IdentNode(tok.valor)
        elif tok.tipo == TT_STRING:
            self.next_token()
            valor_sin_comillas = tok.valor[1:-1]
            return StringNode(valor_sin_comillas)
        else:
            self.error(
                "Se esperaba número, identificador o cadena",
                tok,
                ["número", "identificador", "cadena"],
            )
            return None
