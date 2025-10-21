# Adicionando variáveis
nome = ""
estudante = True
altura = 1.69
ano_atual = 2025
ano_nascimento = ""

# Verificando os tipos de variáveis
print(type(nome))
print(type(estudante))
print(type(altura))
print(type(ano_atual))
print(type(ano_nascimento))

# Solicitando informações
print("")
nome = input("Qual o seu nome? ")
ano_nascimento = input("Qual seu ano de nascimento? ")

# Convertendo tipos de variáveis
nascimento_int = int(ano_nascimento)

# Informando a idade correta
# Usando variáveis inteiras para realizar o cálculo
print("")
idade = ano_atual-nascimento_int
idade_str = str(idade)
print ("Olá, " + nome + ". Atualmente você tem ou irá completar " + idade_str + " anos.")