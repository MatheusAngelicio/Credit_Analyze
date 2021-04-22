from datetime import date
from time import sleep

print()
nome_completo = "Matheus Angelicio"
primeiro_nome = "Matheus"
print('Está é a loja Compre Bem, Seja bem vindo, aqui quem fala é', nome_completo)
print('Agora irei fazer uma análise de crédito, por favor digite as informaçoes que irei solicitar')
print()

# Denifi essas variaveis como global pois vou usar em varios lugares
gasto_limite_global = 0
idade_global = 0
valor_prod_desconto = 0


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

    global gasto_limite_global, idade_global
    gasto_limite_global = gasto_limite
    idade_global = idade


def verificaStatus(credito):
    porcento_sessenta = gasto_limite_global * 0.6
    porcento_noventa = gasto_limite_global * 0.9
    porcento_cem = gasto_limite_global * 1

    if credito <= porcento_sessenta:
        print("Liberado")

    elif porcento_sessenta <= credito and credito <= porcento_noventa:
        print("Liberado ao parcelar em até 2 vezes.")

    elif credito >= porcento_noventa and credito <= porcento_cem:
        print("Liberado ao parcelar em até 3 vezes.")

    else:
        print("Bloqueado!")


def verificaDesconto(v_produto):
    nome_completo_sem_espaco = nome_completo.replace(" ", "")
    quantidade_caractere_nome_completo = len(nome_completo_sem_espaco)

    primeiro_nome_sem_espaco = primeiro_nome.replace(" ", "")
    quantidade_caractere_primeiro_nome = len(primeiro_nome_sem_espaco)

    if quantidade_caractere_nome_completo <= v_produto <= idade_global:
        valor_produto_desconto = v_produto - quantidade_caractere_primeiro_nome
        print("Você terá um desconto de {} reais".format(quantidade_caractere_primeiro_nome))
        print("Seu produto com desconto ficará {:.2f}".format(valor_produto_desconto))
        global valor_prod_desconto
        valor_prod_desconto = valor_produto_desconto


def obterValidarValor():
    v_produto = float(input("Qual o valor : "))
    if v_produto <= 0:
        print("Digite um valor valido")
        return obterValidarValor()
    return v_produto


def cadastroProdutos():

    quantidade_prod = int(input("Quantos produtos deseja cadastrar ? "))
    contador = 0
    total_gasto = 0

    if quantidade_prod <= 0:
        print("Digite um numero valido")
        return cadastroProdutos()

    while contador < quantidade_prod:
        contador = contador + 1
        global valor_prod_desconto

        input("Qual o {}º produto que deseja comprar? : ".format(contador))
        v_produto = obterValidarValor()
        verificaDesconto(v_produto)

        # Se o valor de valor_prod_deconto for diferente te 0, eu pego esse valor e substituo pelo valor de v_produto
        if valor_prod_desconto != 0:
            v_produto = valor_prod_desconto

        total_gasto = total_gasto + v_produto
        print("Você gastou até agora RS{}".format(total_gasto))

        credito = gasto_limite_global - total_gasto
        verificaStatus(total_gasto)

        # Tenho que zerar o valor do desconto para quando entrar no prox loop nao venha com valor setado
        valor_prod_desconto = 0

        if total_gasto >= gasto_limite_global:
            print("Você atingiu o limite")
            break
        else:
            print("Você ainda pode gastar RS{}".format(credito))

        print("-=" * 22)
        print()

    print()
    print("Obrigado por usar minha ferramenta")


obterLimite()
cadastroProdutos()
