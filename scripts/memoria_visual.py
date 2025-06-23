import json

def visualizar_memoria():
    try:
        with open("memoria_afetiva.json", "r", encoding="utf-8") as arquivo:
            memoria = json.load(arquivo)
    except FileNotFoundError:
        print("Arquivo 'memoria_afetiva.json' não encontrado. Crie-o na raiz do projeto com o conteúdo []")
        return

    if not memoria:
        print("Ainda não há interações registradas.")
        return

    # Ordena as entradas da memória pelas datas (das mais recentes para as mais antigas)
    memoria.sort(key=lambda x: x["data"], reverse=True)

    print("----- Diário Afetivo de Anemos -----\n")
    for entrada in memoria:
        print("---------------------------------------")
        print(f"Data      : {entrada['data']}")
        print(f"Texto     : {entrada['texto']}")
        print(f"Emoção    : {entrada['emocao']}")
        print(f"Descrição : {entrada['descricao']}")
        print("---------------------------------------\n")

if __name__ == "__main__":
    visualizar_memoria()