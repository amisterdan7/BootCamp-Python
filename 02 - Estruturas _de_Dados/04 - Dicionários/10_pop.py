contatos = {
    "fulano@gmail.com": {"nome": "Fulano", "telefone": "1234-5678"}
}

resultado = contatos.pop("fulano@gmail.com", "não encontrou")

print(resultado)