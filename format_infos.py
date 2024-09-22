# Formata de acordo com a opção selecionada:
# Pergunta qual documento é se é RG ou CPF/CNPJ (resposta 1 ou 2)
# Recebe o CPF ou RG nao formatado e coloca no formato padrão
# O mesmo para CEP e Telefone

# XXX.XXX.XXX-XX
def format_cpf(cpf): 
    return f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"

# XX.XXX.XXX/0001-XX
def format_cnpj(cnpj): 
    return f"{cnpj[:2]}.{cnpj[2:5]}.{cnpj[5:8]}/{cnpj[8:12]}-{cnpj[12:]}"

# XX.XXX.XXX-X
def format_rg(rg): 
    return f"{rg[:2]}.{rg[2:5]}.{rg[5:8]}-{rg[8:]}"

# XXXXX-XXX
def format_cep(cep):
    return f"{cep[:5]}-{cep[5:]}"

# (XX) XXXXX-XXXX ou (XX) XXXX-XXXX
def format_tel(tel):
    if len(tel) == 11:
        return f"({tel[:2]}) {tel[2:7]}-{tel[7:]}"
    elif len(tel) == 10:
        return f"({tel[:2]}) {tel[2:6]}-{tel[6:]}"
    else:
        return "Número de telefone inválido"

def format_doc():
    tipo = input("Digite 1 para CPF/CNPJ ou 2 para RG: ")

    if tipo == '1':
        doc = input("Digite o CPF/CNPJ: ")
        if len(doc) == 11:
            print("CPF formatado:", format_cpf(doc))
        elif len(doc) == 14:
            print("CNPJ formatado:", format_cnpj(doc))
        else:
            print("Número inválido para CPF/CNPJ.")
    elif tipo == '2':
        rg = input("Digite o RG: ").strip()
        if len(rg) == 9:
            print("RG formatado:", format_rg(rg))
        else:
            print("Número inválido para RG.")
    else:
        print("Opção inválida.")

def format_cep_tel():
    cep = input("Digite o CEP: ")
    print("CEP formatado:", format_cep(cep))

    tel = input("Digite o telefone: ")
    print("Telefone formatado:", format_tel(tel))

format_doc()
format_cep_tel()
