import requests
import json

entrada = input("Você: ")

mensagens = [
    {"role": "system", "content": " "},  # pode até ser em branco se quiser deixar o LM Studio cuidar
    {"role": "user", "content": entrada}
]

payload = {
    "model": "synapsellm-7b-mistral-v0.4-preview2",
    "messages": mensagens,
    "temperature": 0.7,
    "stream": False
}

resposta = requests.post("http://localhost:1234/v1/chat/completions", json=payload)
saida = resposta.json()

print("Anemos:", saida["choices"][0]["message"]["content"])