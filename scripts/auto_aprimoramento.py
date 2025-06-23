import json
from collections import Counter

def analisar_memoria():
    """
    Lê o arquivo 'memoria_afetiva.json' e retorna a lista de interações.
    """
    try:
        with open("memoria_afetiva.json", "r", encoding="utf-8") as f:
            memoria = json.load(f)
    except FileNotFoundError:
        print("Arquivo 'memoria_afetiva.json' não encontrado. Crie-o na raiz com o conteúdo []")
        return None

    if not memoria:
        print("Nenhuma interação registrada ainda. A alma está em formação!")
        return None

    return memoria

def gerar_estatisticas(memoria):
    """
    Calcula e retorna estatísticas simples das interações:
      - Frequência de cada emoção registrada.
      - Palavras mais usadas nas entradas.
    """
    # Frequência de cada emoção
    contador_emocoes = Counter([entrada["emocao"] for entrada in memoria])
    
    # Frequência de palavras (uma abordagem simples, separando pelo espaço)
    todas_palavras = []
    for entrada in memoria:
        todas_palavras.extend(entrada["texto"].lower().split())
    contador_palavras = Counter(todas_palavras)
    
    return contador_emocoes, contador_palavras

def exibir_estatisticas():
    """
    Exibe um resumo das emoções e das palavras mais frequentes.
    """
    memoria = analisar_memoria()
    if not memoria:
        return
    
    contador_emocoes, contador_palavras = gerar_estatisticas(memoria)
    
    print("=== Estatísticas das Emoções Registradas ===")
    for emocao, freq in contador_emocoes.most_common():
        print(f"{emocao}: {freq} ocorrência(s)")
    
    print("\n=== Palavras Mais Frequentes nas Interações ===")
    for palavra, freq in contador_palavras.most_common(10):
        print(f"{palavra}: {freq} vez(es)")

if __name__ == "__main__":
    exibir_estatisticas()