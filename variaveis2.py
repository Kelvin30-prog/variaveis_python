# Criando variáveis
num1 = ""
num2 = ""

# Solicitando números ao usuário
num1 = input("Digite o primeiro número: ")
num2 = input("Digite o segundo número: ")

# Convertendo os tipos de variáveis para realizar o cálculo
num1_int = int(num1)
num2_int = int(num2)

# Realizando o cálculo
print("")
resultado = num1_int + num2_int
resultadostr = str(resultado)
print("O resultado da soma dos dois números é: " + resultadostr)