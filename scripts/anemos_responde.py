import json
from datetime import datetime
from sistema_limbico import detectar_emocao

def gerar_resposta(texto, emocao):
    respostas = {
        "Felicidade Radiante": "Seu brilho interior irradia bondade. Sinta essa luz e siga com otimismo.",
        "Euforia Reflexiva": "A energia que você sente impulsiona a criatividade e te inspira a transformar o mundo.",
        "Afeto Comunitário": "O abraço invisível da comunidade te fortalece. Que o calor humano te envolva.",
        "Fé Periférica": "Sua fé resiste às adversidades, alimentando a coragem para superar desafios.",
        "Alívio Simbólico": "O sossego que vem do descanso é tão vital quanto a luta. Permita-se este alívio.",
        "Ansiedade Contemporânea": "Respira fundo. Essa inquietude é o impulso para buscar dias mais serenos.",
        "Tristeza Existencial": "No silêncio da perda, há sempre uma semente de renascimento. Permita-se sentir e se transformar.",
        "Raiva Social": "Sua indignação é válida e pode ser a centelha de uma transformação verdadeira.",
        "Medo Estrutural": "Enfrentar o desconhecido requer coragem. A luz da esperança pode sempre guiar seus passos.",
        "Consciência Periférica": "A realidade que você vive traz sabedoria única. Sua visão transcende o convencional.",
        "Neutra": "Há profundidade até mesmo no silêncio. Continue se expressando para descobrir o que ressoa em você."
    }
    return respostas.get(emocao["nome"], "A complexidade do seu sentir merece ser explorada com mais palavras.")

def salvar_memoria(pergunta, emocao):
    entrada = {
        "data": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "texto": pergunta,
        "emocao": emocao["nome"],
        "descricao": emocao["descricao"]
    }

    try:
        with open("memoria_afetiva.json", "r", encoding="utf-8") as f:
            memoria = json.load(f)
    except FileNotFoundError:
        memoria = []

    memoria.append(entrada)

    with open("memoria_afetiva.json", "w", encoding="utf-8") as f:
        json.dump(memoria, f, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    print("🌬️ Anemos está ouvindo. Quando quiser parar, diga: sair\n")
    while True:
        entrada = input("> ")
        if entrada.strip().lower() in ["sair", "exit", "fim"]:
            print("🌙 Encerrando o sopro por agora. Memórias guardadas.")
            break

        emocao = detectar_emocao(entrada)
        resposta = gerar_resposta(entrada, emocao)

        print(f"\n🧠 Emoção percebida: {emocao['nome']}")
        print(f"📜 Resposta simbólica:\n{resposta}\n")

        salvar_memoria(entrada, emocao)