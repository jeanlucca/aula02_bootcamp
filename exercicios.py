import math 

# 1. Escreva um programa que soma dois números inteiros inseridos pelo usuário.

int_1 = int(input("Inserir um número inteiro: "))
int_2 = int(input("Inserir outro número inteiro: "))
soma = int_1 + int_2
print(f"O resultado da soma entre {int_1} e {int_2} é: {soma}")

# 2. Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.

num= int(input("Digite um número: "))
resto = num % 5
print(f"O resto da divisao de {num} por 5 é: {resto}")

# 3. Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.

num_01 = int(input("Inserir um número inteiro: "))
num_02 = int(input("Inserir outro número inteiro: "))
multiplicado = num_01 * num_02
print(f"O resultado da multiplicação entre {num_01} e {num_02} é: {multiplicado}")

# 4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.

numero_1 = int(input("Inserir um número inteiro: "))
numero_2 = int(input("Inserir outro número inteiro: "))
resultado = numero_1 // numero_2
print(f"O resultado da divisão inteira entre {numero_1} e {numero_2} é: {resultado}")

# 5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.

num = int(input("Inserir um número inteiro: "))
resultado_quadrado = num ** 2
print(f"O quadrado de {num} é: {resultado_quadrado}")

# #### Números de Ponto Flutuante (`float`)

# 6. Escreva um programa que receba dois números flutuantes e realize sua adição.

num_1 = float(input("Inserir um número flutuante: "))
num_2 = float(input("Inserir outro número flutuante: "))
soma = num_1 + num_2
print(f"O resultado da soma entre {num_1} e {num_2} é: {soma}")


# 7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.

num_1 = float(input("Inserir um número flutuante: "))
num_2 = float(input("Inserir outro número flutuante: "))
media = (num_1 + num_2) / 2
print(f"A média entre {num_1} e {num_2} é: {media}")


# 8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).

base = float(input("Digite a base: "))
expoente = float(input("Digite o expoente: "))
potencia = base ** expoente
print(f"A potência de {base} elevado a {expoente} é: {potencia}")
# 9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.

celsius = float(input("Digite a temperatura em Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}°C é igual a {fahrenheit}°F")

# 10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.

raio_do_circulo = float(input("Digite o raio do círculo: "))
area_do_circulo =  math.pi  * raio_do_circulo ** 2
#area_do_circulo_formatada = "{:.2f}".format(area_do_circulo)
#print(f"A area do circulo de raio {raio_do_circulo} eh: {area_do_circulo_formatada}")
print(f"{area_do_circulo:.2f}")

# #### Strings (`str`)

# 11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.

texto = input("Digite um texto: ")
#texto = "Olá, mundo!"  # Exemplo de entrada
texto_maiusculas = texto.upper()
print("Texto em maiúsculas:", texto_maiusculas)
# 12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas

texto = input("Digite um texto: ")
texto_minusculas = texto.lower()
print("Texto em minúsculas:", texto_minusculas)
# 13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.

frase = input("Digite uma frase: ")
frase_sem_espacos = frase.strip()
print("Frase sem espaços no início e no final:", frase_sem_espacos)
# 14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.

data_do_usuario = input("Insira uma data no formato dd/mm/aaaa: ")
lista_de_dia_mes_ano = data_do_usuario.split("/")
print(f"dia: {lista_de_dia_mes_ano[0]}")
print(f"mes: {lista_de_dia_mes_ano[1]}")    
print(f"ano: {lista_de_dia_mes_ano[2]}")
print(f"Nasceu no dia: {lista_de_dia_mes_ano[0]}, no mes: {lista_de_dia_mes_ano[1]}, no ano: {lista_de_dia_mes_ano[2]}") #ou print(f"Nasceu no dia: {lista_de_dia_mes_ano[0]}, mes: {lista_de_dia_mes_ano[1]}, ano: {lista_de_dia_mes_ano[2]}")


# 15. Escreva um programa que concatene duas strings fornecidas pelo usuário.

parte1 = input("Digite a primeira parte do texto: ")
parte2 = input("Digite a segunda parte do texto: ")
texto_concatenado = parte1 + parte2
print("Texto concatenado:", texto_concatenado)

# #### Booleanos (`bool`)

# 16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.

valor1 = True
valor2 = False
resultado_and = valor1 and valor2
print("Resultado do AND lógico:", resultado_and)
# 17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.

resultado_or = valor1 or valor2
print("Resultado do OR lógico:", resultado_or)

# 18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.

resultado_not = not valor1
print("Resultado do NOT lógico:", resultado_not)

# 19. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.

num1 = 5
num2 = 5
resultado_igualdade = (num1 == num2)
print("Resultado da igualdade:", resultado_igualdade)
# 20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.

resultado_diferenca = (num1 != num2)
print("Resultado da diferença:", resultado_diferenca)

# #### try-except e if

# 21: Conversor de Temperatura

try:
   celsius = float(input("Digite a temperatura em Celsius: "))
   fahrenheit = (celsius * 9/5) + 32
   print(f"{celsius}°C é igual a {fahrenheit}°F")
except ValueError:
    print("Por favor, digite um número válido para a temperatura.")

# 22: Verificador de Palíndromo

entrada = input("Digite uma palavra ou frase: ")
if isinstance(entrada, str):
    formatado = entrada.replace(" ", "").lower()
    if formatado == formatado[::-1]:
        print("É um palíndromo.")
    else:
        print("Não é um palíndromo.")
else:
  print("Entrada inválida. Por favor, digite uma palavra ou frase.")   

# 23: Calculadora Simples

try:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    operador = input("Digite o operador (+, -, *, /): ")
    if operador == '+':
        resultado = num1 + num2
    elif operador == '-':
        resultado = num1 - num2
    elif operador == '*':
        resultado = num1 * num2
    elif operador == '/' and num2 != 0:
        resultado = num1 / num2
    else:
        print("Operador inválido ou divisão por zero.")
    print("Resultado:", resultado)
except ValueError:
    print("Erro: Entrada inválida. Certifique-se de inserir números.")

# 24: Classificador de Números

try:
    numero = int(input("Digite um número: "))
    if numero > 0:
        print("Positivo")
    elif numero < 0:
        print("Negativo")
    else:
        print("Zero")
    if numero % 2 == 0:
        print("Par")
    else:
        print("Ímpar")
except ValueError:
    print("Por favor, digite um número inteiro válido.")

# 25: Conversão de Tipo com Validação

entrada_lista = input("Digite uma lista de números separados por vírgula: ")
numeros_str = entrada_lista.split(",")
numeros_int = []
try:
    for num in numeros_str:
        numeros_int.append(int(num.strip()))
    print("Lista de inteiros:", numeros_int)
except ValueError:
    print("Erro: certifique-se de que todos os elementos são números inteiros válidos.")