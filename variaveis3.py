# Criando variáveis com o seu tipo já definido, desta forma não será necessário alterar no decorrer do código
ano_atual = int
data_nascimento = int

# solicitando informações
ano_atual = int(input("Digite o ano que você está: "))
data_nascimento = int(input("Qual o ano da sua data de nascimento? "))

# Realizando a operação
print("")
resultado = str(ano_atual - data_nascimento)
print("De acordo com as informações dadas, sua idade é: " + resultado + " anos.")