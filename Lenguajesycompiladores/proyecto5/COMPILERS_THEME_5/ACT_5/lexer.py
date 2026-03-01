import re
from token import (
    Token,
    TT_KEYWORD,
    TT_IDENT,
    TT_NUMBER,
    TT_OPERATOR,
    TT_PAREN,
    TT_SEMICOLON,
    TT_WHITESPACE,
    TT_STRING,
    TT_UNKNOWN,
)
from levenshtein import confidence


class Lexer:
    keywords = {"if", "else", "print"}

    token_specs = [
        (TT_KEYWORD, r"if|else|print"),
        (TT_IDENT, r"[a-zA-Z_][a-zA-Z0-9_]*"),
        (TT_NUMBER, r"\d+"),
        (TT_OPERATOR, r"[=><]"),
        (TT_PAREN, r"[()]"),
        (TT_SEMICOLON, r";"),
        (TT_STRING, r'"[^"]*"'),
        (TT_WHITESPACE, r"\s+"),
        (TT_UNKNOWN, r"\S+"),
    ]

    master_regex = "|".join(f"(?P<{tipo}>{patron})" for tipo, patron in token_specs)
    master_re = re.compile(master_regex)

    def get_tokens(self, code):
        tokens_raw = []
        linea = 1
        columna = 1
        pos = 0

        while pos < len(code):
            match = self.master_re.match(code, pos)
            if not match:
                char = code[pos]
                tok = Token(TT_UNKNOWN, char, linea, columna)
                tokens_raw.append(tok)
                columna += 1
                pos += 1
                continue

            tipo = match.lastgroup
            valor = match.group()

            if tipo == TT_WHITESPACE:
                lineas_nuevas = valor.count("\n")
                if lineas_nuevas:
                    linea += lineas_nuevas
                    columna = 1
                else:
                    columna += len(valor)
            else:
                tok = Token(tipo, valor, linea, columna)
                tokens_raw.append(tok)
                columna += len(valor)

            pos = match.end()

        tokens_corregidos = []
        sugerencias = []

        for tok in tokens_raw:
            if tok.tipo == TT_IDENT:
                tok_corregido, sug = self._corregir_ident(tok)
                if sug:
                    sugerencias.append(sug)
                tokens_corregidos.append(tok_corregido)
            elif tok.tipo == TT_UNKNOWN:
                tok_corregido, sug = self._corregir_unknown(tok)
                if sug:
                    sugerencias.append(sug)
                tokens_corregidos.append(tok_corregido)
            else:
                tokens_corregidos.append(tok)

        return tokens_corregidos, sugerencias

    def _corregir_ident(self, token):
        palabra = token.valor
        if palabra in self.keywords:
            return token, None

        mejor_conf = 0
        mejor_kw = None
        for kw in self.keywords:
            conf = confidence(palabra, kw)
            if conf > mejor_conf:
                mejor_conf = conf
                mejor_kw = kw

        if mejor_conf >= 0.8:
            nuevo_token = Token(TT_KEYWORD, mejor_kw, token.linea, token.columna)
            sugerencia = (
                f"Sugerencia: '{palabra}' -> '{mejor_kw}' (confianza {mejor_conf:.2f})"
            )
            return nuevo_token, sugerencia
        else:
            return token, None

    def _corregir_unknown(self, token):
        palabra = token.valor
        mejor_conf = 0
        mejor_kw = None
        for kw in self.keywords:
            conf = confidence(palabra, kw)
            if conf > mejor_conf:
                mejor_conf = conf
                mejor_kw = kw

        if mejor_conf >= 0.8:
            nuevo_token = Token(TT_KEYWORD, mejor_kw, token.linea, token.columna)
            sugerencia = (
                f"Sugerencia: '{palabra}' -> '{mejor_kw}' (confianza {mejor_conf:.2f})"
            )
            return nuevo_token, sugerencia
        else:
            resultado_ia = self._consultar_ia(palabra)
            if resultado_ia:
                tipo_sug, valor_sug = resultado_ia
                nuevo_token = Token(tipo_sug, valor_sug, token.linea, token.columna)
                sugerencia = (
                    f"Sugerencia IA: '{palabra}' -> '{valor_sug}' (tipo {tipo_sug})"
                )
                return nuevo_token, sugerencia
            else:
                return token, None

    def _consultar_ia(self, palabra):
        if palabra == "prnt":
            return (TT_KEYWORD, "print")
        return None
