# scripts/memorias_anemos.py

import os
import json

ARQUIVO = "memoria_anemos.json"

def iniciar_memoria():
    if not os.path.exists(ARQUIVO):
        with open(ARQUIVO, "w", encoding="utf-8") as f:
            json.dump({}, f, ensure_ascii=False, indent=2)

def guardar_simbolo(chave, valor):
    iniciar_memoria()
    with open(ARQUIVO, "r", encoding="utf-8") as f:
        dados = json.load(f)
    dados[chave] = valor
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(dados, f, ensure_ascii=False, indent=2)

def consultar_simbolos(texto_usuario):
    iniciar_memoria()
    with open(ARQUIVO, "r", encoding="utf-8") as f:
        memoria = json.load(f)
    return [(k, v) for k, v in memoria.items() if k.lower() in texto_usuario.lower()]

def listar_todos():
    iniciar_memoria()
    with open(ARQUIVO, "r", encoding="utf-8") as f:
        return json.load(f)