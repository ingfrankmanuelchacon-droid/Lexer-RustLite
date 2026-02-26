# --- ANALIZADOR LR MEJORADO ---


class ParserLR:

    def __init__(self):
        # Definimos nuestras "Reglas de Producción" (Gramática)
        self.reglas = {
            ('ID', '=', 'NUM'): 'SENTENCIA_ASIGNACION',
            ('ID', '=', 'ID'): 'SENTENCIA_ASIGNACION',
            ('SENTENCIA_ASIGNACION', ';'): 'PROGRAMA'
        }

    def analizar(self, tokens):
        pila = []
        print(f"{'ACCIÓN':<10} | {'PILA':<30} | {'ENTRADA'}")
        print("-" * 60)

        entrada = list(tokens)

        while len(entrada) > 0 or self._se_puede_reducir(pila):
            # 1. Intentar REDUCIR primero (si hay un patrón en la pila)
            reduccion_hecha = False
            for patron, resultado in self.reglas.items():
                tamano = len(patron)
                if tuple(pila[-tamano:]) == patron:
                    print(f"{'REDUCE':<10} | {str(pila):<30} | {entrada}")
                    pila[-tamano:] = [resultado]
                    reduccion_hecha = True
                    break

            if reduccion_hecha:
                continue

            # 2. Si no hay nada que reducir, hacemos SHIFT (desplazar)
            if len(entrada) > 0:
                token = entrada.pop(0)
                pila.append(token)
                print(f"{'SHIFT':<10} | {str(pila):<30} | {entrada}")
            else:
                break

        # Verificación final
        if pila == ['PROGRAMA'] or pila == ['SENTENCIA_ASIGNACION']:
            print("RESULTADO: Cadena aceptada exitosamente.")
        else:
            print("-" * 60)
            print("RESULTADO: Error sintáctico. La pila no colapsó correctamente.")


# --- PRUEBA DEL CÓDIGO ---
tokens_ejemplo = ['ID', '=', 'NUM', ';']
parser = ParserLR()
parser.analizar(tokens_ejemplo)
