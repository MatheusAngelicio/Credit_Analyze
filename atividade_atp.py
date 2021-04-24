from datetime import date
from time import sleep

print()
nome_completo = "Matheus Angelicio"
primeiro_nome = "Matheus"
print('Está é a loja Compre Bem, Seja bem vindo, aqui quem fala é', nome_completo)
print('Agora irei fazer uma análise de crédito, por favor digite as informaçoes que irei solicitar')
print()


def obterLimite():
    cargo = input('Informe seu cargo: ')
    salario = float(input('Informe seu salario: '))
    ano_nasc = int(input('Informe o ano de nascimento: '))

    print()
    print("-=" * 8 + " PROCESSANDO " + "-=" * 8)
    sleep(1)
    print()

    print('Seu cargo é: {}'.format(cargo))
    print('Seu salario e: {}'.format(salario))
    print('Seu ano de nascimento é: {}'.format(ano_nasc))

    ano_atual = date.today().year
    idade = ano_atual - ano_nasc
    gasto_limite = salario * (idade / 1000) + 100  # calculado da seguinte forma: [salário x (idade / 1.000)] + 100.

    print('Sua idade é: {} '.format(idade))
    print('Você podera gastar na minha loja: RS{:.2f} '.format(gasto_limite))
    print()

    return gasto_limite, idade


def verificaStatus(credito, gasto_limite):
    porcento_sessenta = gasto_limite * 0.6
    porcento_noventa = gasto_limite * 0.9
    porcento_cem = gasto_limite * 1

    if credito <= porcento_sessenta:
        print("Liberado")

    elif porcento_sessenta <= credito and credito <= porcento_noventa:
        print("Liberado ao parcelar em até 2 vezes.")

    elif credito >= porcento_noventa and credito <= porcento_cem:
        print("Liberado ao parcelar em até 3 vezes.")

    else:
        print("Bloqueado!")


def verificaDesconto(v_produto, idade):
    nome_completo_sem_espaco = nome_completo.replace(" ", "")
    quantidade_caractere_nome_completo = len(nome_completo_sem_espaco)

    primeiro_nome_sem_espaco = primeiro_nome.replace(" ", "")
    quantidade_caractere_primeiro_nome = len(primeiro_nome_sem_espaco)
    valor_prod_desconto = 0

    if quantidade_caractere_nome_completo <= v_produto <= idade:
        valor_prod_desconto = v_produto - quantidade_caractere_primeiro_nome
        print("Você terá um desconto de {} reais".format(quantidade_caractere_primeiro_nome))
        print("Seu produto com desconto ficará {:.2f}".format(valor_prod_desconto))

    else:
        # Preciso zerar o valor da variavel, pq se ela receber o valor de desconto, na proxima vez que eu verificar o desconto e nao tiver
        # desconto, tenho que mandar 0 para funcao
        valor_prod_desconto = 0

    return valor_prod_desconto


def obterValidarValor():
    v_produto = float(input("Qual o valor : "))
    if v_produto <= 0:
        print("Digite um valor valido")
        return obterValidarValor()
    return v_produto


def fimOperacao(sobra, total_gasto):
    if sobra >= 0:
        print("Ao final da operação você gastou RS{} e sobrou RS{} do seu dinheiro".format(total_gasto, sobra))
    else:
        print("Vish você não tem esse dinheiro, iremos encerrar a operação !!")


def cadastroProdutos(gasto_limite, idade):
    quantidade_prod = int(input("Quantos produtos deseja cadastrar ? "))
    contador = 0
    total_gasto = 0

    if quantidade_prod <= 0:
        print("Digite um numero valido")
        return cadastroProdutos(gasto_limite,idade)

    while contador < quantidade_prod:
        contador = contador + 1

        input("Qual o {}º produto que deseja comprar? : ".format(contador))
        v_produto = obterValidarValor()

        valor_prod_desconto = verificaDesconto(v_produto, idade)

        # Se o valor de valor_prod_deconto for diferente de 0, eu pego esse valor e substituo pelo valor de v_produto
        if valor_prod_desconto != 0:
            v_produto = valor_prod_desconto

        total_gasto = total_gasto + v_produto
        print("Você gastou até agora RS{}".format(total_gasto))

        credito = gasto_limite - total_gasto
        verificaStatus(total_gasto,gasto_limite)

        if total_gasto >= gasto_limite:
            print("Você atingiu o limite")
            break
        else:
            print("Você ainda pode gastar RS{}".format(credito))

        print("-=" * 22)
        print()

    sobra = gasto_limite - total_gasto
    fimOperacao(sobra, total_gasto)

    print()
    print("Obrigado por usar minha ferramenta")


gasto_limite, idade = obterLimite()

cadastroProdutos(gasto_limite, idade)
