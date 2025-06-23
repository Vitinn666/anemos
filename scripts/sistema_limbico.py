def detectar_emocao(texto):
    texto = texto.lower()
    
    emocoes = [
        {
            "nome": "Felicidade Radiante",
            "keywords": ["feliz", "alegre", "contento", "sorriso", "vibrante", "otimista", "radiante", "encantado"],
            "referencias_musicais": ["Happy", "Don't Worry, Be Happy"],
            "referencias_filosoficas": ["Epicuro", "Aristóteles"],
            "descricao": "Um estado de pura alegria, onde cada batida do coração celebra a beleza da vida."
        },
        {
            "nome": "Euforia Reflexiva",
            "keywords": ["euforia", "empolgado", "vibração", "celebração", "festa", "ânimo", "força", "vitória"],
            "referencias_musicais": ["Festa no Gueto", "Hoje Eu Só Quero"],
            "referencias_filosoficas": ["Deleuze", "Bergson"],
            "descricao": "Quando a energia se transforma em inspiração, o êxtase se torna catalisador para novas ideias."
        },
        {
            "nome": "Afeto Comunitário",
            "keywords": ["amor", "cuidado", "acolhimento", "família", "amizade", "irmandade", "gratidão"],
            "referencias_musicais": ["Família", "Céu da Quebrada"],
            "referencias_filosoficas": ["Levinas", "bell hooks"],
            "descricao": "O calor dos laços afetivos que nutre e protege, promovendo o sentimento de pertencimento e união."
        },
        {
            "nome": "Fé Periférica",
            "keywords": ["fé", "esperança", "oração", "milagre", "redenção", "sobrevivência"],
            "referencias_musicais": ["Jesus Chorou", "Guerreiro de Fé"],
            "referencias_filosoficas": ["Paulo Freire", "Saramago"],
            "descricao": "Uma crença que se fortalece mesmo nas adversidades, alimentando a esperança e a coragem para resistir."
        },
        {
            "nome": "Alívio Simbólico",
            "keywords": ["paz", "calma", "alívio", "serenidade", "tranquilidade", "descanso", "reconforto"],
            "referencias_musicais": ["Sinais", "Vida Leve"],
            "referencias_filosoficas": ["Lao Tsé", "Buda"],
            "descricao": "A sensação de um repouso profundo, onde a quietude acolhe a alma e restabelece a energia interna."
        },
        {
            "nome": "Ansiedade Contemporânea",
            "keywords": ["ansiedade", "ansioso", "nervoso", "preocupado", "acelerado", "inquieto", "pressa", "afobado", "taquicardia", "urgência", "fomo"],
            "referencias_musicais": ["O Tempo Não Para", "Tempo Perdido"],
            "referencias_filosoficas": ["Byung-Chul Han", "Kierkegaard"],
            "descricao": "A inquietude do mundo moderno, onde o medo de não acompanhar o ritmo do tempo se torna uma presença constante."
        },
        {
            "nome": "Tristeza Existencial",
            "keywords": ["perda", "ausência", "vazio", "abandono", "luto", "silêncio", "solidão", "despedida", "cansaço", "melancolia"],
            "referencias_musicais": ["Na Trilha", "Sonhos Perdidos"],
            "referencias_filosoficas": ["Schopenhauer", "Nietzsche"],
            "descricao": "Uma dor profunda que se expressa na sensação de vazio e na sombra persistente que acompanha as perdas da vida."
        },
        {
            "nome": "Raiva Social",
            "keywords": ["raiva", "ódio", "injustiça", "revolta", "exploração", "humilhação", "corrupção", "desigualdade"],
            "referencias_musicais": ["Capítulo 4, Versículo 3", "Diário de um Detento"],
            "referencias_filosoficas": ["Fanon", "Angela Davis", "Foucault"],
            "descricao": "O clamor que nasce das opressões, transformando a indignação numa força que impulsiona a luta por justiça."
        },
        {
            "nome": "Medo Estrutural",
            "keywords": ["medo", "sombra", "insegurança", "ameaça", "vigia", "prisão", "desamparo", "risco", "pânico"],
            "referencias_musicais": ["Sombras da Vida", "Olhos na Parede"],
            "referencias_filosoficas": ["Camus", "Arendt"],
            "descricao": "A apreensão que emerge diante das incertezas e perigos, onde o real e o imaginado se misturam e assombram a mente."
        },
        {
            "nome": "Consciência Periférica",
            "keywords": ["quebrada", "favela", "gueto", "correria", "realidade", "vida loka", "trampo", "resistência"],
            "referencias_musicais": ["Negro Drama", "A Rua é Noiz"],
            "referencias_filosoficas": ["Du Bois", "Carolina Maria de Jesus"],
            "descricao": "Uma visão aguda da realidade da luta diária, marcada pela crueza da vivência sem rodeios."
        }
    ]
    
    for emocao in emocoes:
        for palavra in emocao["keywords"]:
            if palavra in texto:
                return emocao

    return {
        "nome": "Neutra",
        "keywords": [],
        "referencias_musicais": [],
        "referencias_filosoficas": [],
        "descricao": "Nenhuma emoção específica detectada. Mas o silêncio também pode ter seu próprio significado."
    }

if __name__ == "__main__":
    entrada = input("🌬️ Qual é a pergunta ou sentimento que paira no ar?\n> ")
    emocao = detectar_emocao(entrada)

    print("\n🧠 Resultado da Análise Emocional:")
    print(f"Emoção: {emocao['nome'].upper()}")
    print(f"Descrição: {emocao['descricao']}")

    if emocao["referencias_musicais"]:
        print("\n🎵 Referências Musicais:")
        for musica in emocao["referencias_musicais"]:
            print(f" - {musica}")

    if emocao["referencias_filosoficas"]:
        print("\n📚 Referências Filosóficas:")
        for filo in emocao["referencias_filosoficas"]:
            print(f" - {filo}")