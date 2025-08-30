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



for chave in contatos:
    print(chave, contatos[chave])

#print("-*" * 50)

#for chave, valor in contatos.items():
#   print(chave, valor)