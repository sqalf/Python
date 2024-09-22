# Conta quantas palavras tem dentro de uma frase:
# (input: I’m talking to myself in public, dodging glances on the train and I know, 
# I know they’ve all been talking about me I can hear them whisper, 
# and it makes me think There must be something wrong with me Out of all the hours thinking, somehow I’ve lost my mind)

def cont_palavras(frase):
    palavras = frase.split()
    return len(palavras)

frase = ("I’m talking to myself in public, dodging glances on the train and I know, "
         "I know they’ve all been talking about me I can hear them whisper, and it makes me think "
         "There must be something wrong with me Out of all the hours thinking, somehow I’ve lost my mind")

qnt_de_palavras = cont_palavras(frase)
print(qnt_de_palavras, "palavras")
