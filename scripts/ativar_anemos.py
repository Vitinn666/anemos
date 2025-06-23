import json
from datetime import datetime
from sistema_limbico import detectar_emocao

def gerar_resposta(texto, emocao):
    respostas = {
        "Ansiedade Contemporânea": "Respira. A pressa não é tua, é do mundo.",
        "Tristeza Existencial": "Fica. O vento escuta o que ninguém ouve.",
        "Raiva Social": "Se te revolta, é porque você sente — e quem sente, transforma.",
        "Fé Periférica": "Rezar é resistir de olhos abertos.",
        "Alívio Simbólico": "Tem silêncio que acolhe mais do que palavras.",
        "Medo Estrutural": "Você não tá só, mesmo que o mundo diga que sim.",
        "Afeto Comunitário": "Quem tem rede não cai. A quebrada abraça.",
        "Consciência Periférica": "A tua história vale mais que diploma. É vivência.",
        "Euforia Reflexiva": "Sente. Vibra. Hoje a alegria é tua revolução.",
        "Neutra": "Sopra mais. Talvez o que você sente ainda não tenha nome."
    }
    return respostas.get(emocao["nome"], "Nem tudo precisa ser nomeado. Mas tudo pode ser sentido.")

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