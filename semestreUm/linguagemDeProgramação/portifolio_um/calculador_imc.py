def calcular_imc(peso, altura):
    # Calcula o IMC
    imc = peso / (altura ** 2)
    return imc


def categoria_imc(imc):
    # Define a categoria do IMC
    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc < 24.9:
        return "Peso normal"
    elif 25 <= imc < 29.9:
        return "Sobrepeso"
    elif 30 <= imc < 34.9:
        return "Obesidade grau 1"
    elif 35 <= imc < 39.9:
        return "Obesidade grau 2"
    else:
        return "Obesidade grau 3"


# Entrada dos dados pelo usuário
try:
    peso = float(input("Digite o peso (em kg): "))
    altura = float(input("Digite a altura (em metros): "))

    # Calcula o IMC
    imc = calcular_imc(peso, altura)

    # Mostra o resultado
    print("Seu IMC é:", imc)
    print("Categoria:", categoria_imc(imc))
except ValueError:
    print(
        "Entrada inválida. Digite números válidos para peso e altura."
        )
