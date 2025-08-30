contatos = {
    "amigo": {
        "nome": "Carlos",
        "telefone": "1234-5678"
    },
    "familia": {
        "nome": "Maria",
        "telefone": "9876-5432"
    },
    "trabalho": {
        "nome": "Ana",
        "telefone": "5555-1234",
        "profissao": "Desenvolvedora"
    }
    
}

nome = contatos["familia"]["nome"]
telefone = contatos["familia"]["telefone"]
profissao = contatos["trabalho"]["profissao"]

print(f"Nome: {nome}")
print(f"Telefone: {telefone}")
print(f"Profissão: {profissao}")
