# Projeto calculadora

def soma(n1, n2):
    return n1 + n2

def subtracao(n1, n2):
    return n1 - n2

def multiplicacao(n1, n2):
    return n1 * n2

def divisao(n1, n2):
    if n2 == 0:
        return "Erro: divisão por zero!"
    return n1 / n2


calculo = {"+": soma,
           "-": subtracao,
           "*": multiplicacao,
           "/": divisao,
}

print("Bem-vindo à Calculadora Python! 💡")

num1 = float(input("Digite um número: "))
sinal = input("Informe o operador para o seu calculo: +(soma), -(subtração), *(multiplicação), /(divisão)")
num2 = float(input("Digite outro número: "))


resul = calculo[sinal](n1=num1, n2=num2)
print(resul)

resultado = 0.0

novo_calculo = "s"

while novo_calculo == "s":

    novo_calculo = input("Deseja realizar um novo calculo? s(sim) / n(não)").lower()

    if novo_calculo == "s":
        resultado = float(input(("Digite um número: ")))
        sinal = input("Informe o operador para o seu calculo: +(soma), -(subtração), *(multiplicação), /(divisão)")
        resul = calculo[sinal](n1=resul, n2=resultado)
        print(resul)
    else:
        print("Calculadora encerrada. Até a próxima! 🧠💻")

