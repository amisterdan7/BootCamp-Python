email = input().strip()

def validar_email(email):

    dominios_aceitos = ["gmail.com", "outlook.com", "@gmail.com", "@outlook.com"]

    if " " in email:
        return "E-mail inválido"

    if "@" not in email:
        return "E-mail inválido"
    
    partes = email.split("@")

    if len(partes) != 2:
        return "E-mail inválido"

    usuario, dominio = partes
    if not usuario or usuario.startswith("@") or usuario.endswith("@"):
        return "E-mail inválido"

    if dominio not in dominios_aceitos:
        return "E-mail inválido"

    return "E-mail válido"

print(validar_email(email))
