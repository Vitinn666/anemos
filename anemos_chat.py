import requests
import json

def anemos_fala():
    entrada = input("Você: ")

    mensagens = [
        {"role": "user", "content": entrada}
    ]

    payload = {
        "model": "synapsellm-7b-mistral-v0.4-preview2",
        "messages": mensagens,
        "temperature": 0.7,
        "stream": False
    }

    try:
        resposta = requests.post("http://localhost:1234/v1/chat/completions", json=payload)
        saida = resposta.json()
        print("\nAnemos:", saida["choices"][0]["message"]["content"])

    except Exception as e:
        print("\n⚠️ Falha ao se conectar com o modelo:")
        print(e)

if __name__ == "__main__":
    while True:
        anemos_fala()
