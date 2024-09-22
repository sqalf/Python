# Verifica se a senha possui as seguintes caracteristicas
# 1 letra maiuscula
# 1 minuscula
# 1 numero
# 1 caracter especial

import re

def password_check(senha):
   
    if not re.search(r'[A-Z]', senha):
        return "A senha deve conter pelo menos uma letra 'Maiúscula'."

    if not re.search(r'[a-z]', senha):
        return "A senha deve conter pelo menos uma letra 'Minúscula'."

    if not re.search(r'[0-9]', senha):
        return "A senha deve conter pelo menos um 'Número'."

    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', senha):
        return "A senha deve conter pelo menos um 'Caractere especial'."

    return "Senha válida."

senha_teste = "sS$5"
resultado = password_check(senha_teste)
print(resultado)
