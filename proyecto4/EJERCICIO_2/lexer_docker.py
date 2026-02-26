import re

class DockerLexer:
    def __init__(self):
        # Definición de patrones (Token Name, Regex)
        self.token_specification = [
            ('COMMENT',     r'#.*'),
            ('INSTRUCTION', r'\b(FROM|RUN|CMD|LABEL|EXPOSE|ENV|ADD|COPY|ENTRYPOINT|VOLUME|USER|WORKDIR|ARG|STOPSIGNAL|HEALTHCHECK|SHELL)\b'), # Palabras clave
            ('ARGUMENT',    r'(?<=\s).+'),
            ('NEWLINE',     r'\n'),
            ('SKIP',        r'[ \t]+'),
            ('MISMATCH',    r'.'),    
        ]
        # Compilación de la regex maestra
        self.regex_pattern = '|'.join('(?P<%s>%s)' % pair for pair in self.token_specification)

    def tokenize(self, code):
        tokens = []
        for mo in re.finditer(self.regex_pattern, code, re.IGNORECASE):
            kind = mo.lastgroup
            value = mo.group()
            if kind == 'NEWLINE' or kind == 'SKIP':
                continue
            elif kind == 'MISMATCH':
                print(f'Error léxico: Caracter inesperado {value!r}')
            else:
                tokens.append((kind, value.strip()))
        return tokens

lexer = DockerLexer()