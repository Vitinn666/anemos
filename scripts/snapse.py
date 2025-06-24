# scripts/snapse.py

simbolos = {}

def learn(conceito, significado):
    simbolos[conceito.lower()] = significado

def query(texto):
    resultados = []
    for conceito, significado in simbolos.items():
        if conceito.lower() in texto.lower():
            resultados.append((conceito, significado))
    return resultados

def listar_todos():
    return simbolos