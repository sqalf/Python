# Faça um algoritmo que leia o .txt e imprima quantas vezes aparece ERRO

def contador(txt):
    try:
        with open(txt, 'r') as txt:
            content = txt.read()
            
            count = content.upper().count('ERRO')
            
            print(f'A palavra "ERRO" aparece {count} vezes.')
    
    except FileNotFoundError:
        print(f'Arquivo {txt} não encontrado.')
    except Exception as e:
        print(f'Ocorreu um erro: {e}')

txt = 'teste1.txt'
contador(txt)