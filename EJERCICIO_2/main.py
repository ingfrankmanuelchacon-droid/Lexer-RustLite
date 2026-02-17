# main.py
from lexer_docker import DockerLexer


def ejecutar_pruebas():
    lexer = DockerLexer()

    casos_de_prueba = [
        {
            "nombre": "CASO 1: Dockerfile Básico (Node.js)",
            "contenido": """
FROM node:18
WORKDIR /app
COPY . .
RUN npm install
CMD ["node", "index.js"]
            """,
        },
        {
            "nombre": "CASO 2: Variables de Entorno y Comentarios",
            "contenido": """
# Definición de imagen base
FROM python:3.9-slim
ENV APP_HOME=/home/app
WORKDIR $APP_HOME
LABEL version="1.0"
            """,
        },
        {
            "nombre": "CASO 3: Construcción Multi-etapa (Multi-stage)",
            "contenido": """
FROM golang:1.16 AS builder
WORKDIR /go/src/app
RUN go build -o myapp
FROM alpine:latest
COPY --from=builder /go/src/app/myapp .
ENTRYPOINT ["./myapp"]
            """,
        },
    ]

    print("==================================================")
    print("      REPORTE DE EJECUCIÓN DEL LEXER DOCKER       ")
    print("==================================================\n")

    for i, caso in enumerate(casos_de_prueba, 1):
        print(f"--- {caso['nombre']} ---")
        print("CONTENIDO:")
        print(caso["contenido"].strip())
        print("\nTOKENS GENERADOS:")

        tokens = lexer.tokenize(caso["contenido"])

        # Formateo de tabla simple para el informe
        print(f"{'TIPO DE TOKEN':<15} | {'VALOR CARGADO'}")
        print("-" * 40)
        for tipo, valor in tokens:
            print(f"{tipo:<15} | {valor}")

        print("\n" + "=" * 50 + "\n")


if __name__ == "__main__":
    ejecutar_pruebas()
