contatos = {
    "fulano@gmail.com": {"nome": "Fulano", "telefone": "1234-5678"}
}

copia = contatos.copy()

copia["fulano@gmail.com"]= {"nome": "Fulano"}

print(contatos)
print(copia)