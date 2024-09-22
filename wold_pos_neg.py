# Recebe 2 listas:
# palavras_positivas = ["bom", "ótimo", "excelente", "feliz", "alegre"]
# palavras_negativas = ["ruim", "horrível", "péssimo", "triste", "deprimido"]
# Identifique se o input do usuario é uma palavra positiva ou negativa

palavras_positivas = ["bom", "ótimo", "excelente", "feliz", "alegre"]
palavras_negativas = ["ruim", "horrível", "péssimo", "triste", "deprimido"]

def identific(palavra):
    if palavra.lower() in palavras_positivas:
        return "A palavra é positiva."
    elif palavra.lower() in palavras_negativas:
        return "A palavra é negativa."
    else:
        return "A palavra não está em nenhuma das listas."

palavra = input("Digite uma palavra: ")
resultado = identific(palavra)
print(resultado)
