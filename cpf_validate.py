# Valida um cpf

def cpf_check(cpf):

    cpf = ''.join(filter(str.isdigit, cpf))

    if len(cpf) != 11:
        return False

    if cpf == cpf[0] * 11:
        return False

    def calc_digito(cpf, opt):
        soma = sum(int(cpf[i]) * opt[i] for i in range(len(opt)))
        resto = soma % 11
        return 0 if resto < 2 else 11 - resto

    opt1 = list(range(10, 1, -1))
    digito1 = calc_digito(cpf[:9], opt1)

    opt2 = list(range(11, 1, -1))
    digito2 = calc_digito(cpf[:10], opt2)

    return cpf[-2:] == f'{digito1}{digito2}'

cpf_teste = '059.456.789-09'
resultado = cpf_check(cpf_teste)
print(f'O CPF {cpf_teste} é {"válido" if resultado else "inválido"}.')
