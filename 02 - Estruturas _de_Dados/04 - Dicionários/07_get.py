contatos = {
    "arrasca": {"nome": "Arrasca", "telefone": "1234-5678"}
}

print(contatos.get("chave")) # None
print(contatos.get("chave", {})) # Retorna um dicionário vazio
print(contatos.get("arrasca", {})) # Retorna o dicionário do contato

