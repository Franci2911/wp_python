'''
1. Inteiros (int)
Métodos e operações:
+ (adição)
- (subtração)
* (multiplicação)
// (divisão inteira)
% (módulo - resto da divisão)

2. Números de Ponto Flutuante (float)
Métodos e operações:
+ (adição)
- (subtração)
* (multiplicação)
/ (divisão)
** (potenciação)

3. Strings (str)
Métodos e operações:
.upper() (converte para maiúsculas)
.lower() (converte para minúsculas)
.strip() (remove espaços em branco no início e no final)
.split(sep) (divide a string em uma lista, utilizando sep como delimitador)
+ (concatenação de strings)

4. Booleanos (bool)
Operações lógicas:
and (E lógico)
or (OU lógico)
not (NÃO lógico)
== (igualdade)
!= (diferença)'''


# EXERCICIOS

# 1 Escreva um programa que soma dois números inteiros inseridos pelo usuário.
#n1 = int(input("Digite o primeiro número:"))
#n2 = int(input("Digite o segundo número: "))
#retorno = (n1+n2)
#print(f"A soma entre o primeiro número:{n1} e o segundo número:{n2} é igual a:{retorno}")


# 2 Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.
#n01 = int(input("Digite um numero:"))
#retorno_n01 = (n01 % 5)
#print(f"O resto da divisão é: {retorno_n01}")

# 3 Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.
#num01 = int(input("Digite um número:"))
#num02 = float(input("Digite mais um número"))
#resultado03 = (num01 * num02)
#print(f"A multiplicação entre os números é: {resultado03}")

# 4 Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.
#n1 = int(input("Digite o primeiro número: "))
#n2 = int(input("Digite o segundo número: "))
#rs = (n1 // n2)
#print(f"O resultado é {rs}")

# 5 Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.
#n1 = int(input("Digite um número: "))
#rs = n1 ** 2
#print(f"resultado: {rs}")


# 6 Escreva um programa que receba dois números flutuantes e realize sua adição.
#n1 = float(input("Digite um número: "))
#n2 = float(input("Digite o segundo número"))
#rs = (n1+n2)
#print(f"O resultado é {rs}")

# 7 Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.
#n1 = float(input("Digite um número: "))
#n2 = float(input("Digite o segundo número: "))
#rs = (n1+n2)/2
#print(f"A média é: {rs}")

# 8 Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuári
#n1 = float(input("Digite um número: "))
#n2 = int(input("Digite o expoente: "))
#rs = n1 ** n2
#print(f"O resultado é: {rs}")

# 9 Faça um programa que converta a temperatura de Celsius para Fahrenheit.
#celsius = float(input("Digite uma temperatura em Celsius: "))
#fagrenheit = (celsius * 9/5) + 32
#print(f"A temperatura em celsius:{celsius}°C, é igual a:{fagrenheit}°F")

# 10 Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.
#raio = float(input("Digite o raio do círculo: "))
#raio = 5.0  # Exemplo de entrada
#area = 3.14159 * raio ** 2
#print("A área do círculo é:", area)


# 11 Escreva um programa que receba uma string do usuário e a converta para maiúsculas.
#nome = input("Qual é o seu nome: ")
#print(nome.upper())

# 12 Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.
#nome = input("Qual é o seu nome: ")
#print(nome.lower())

# 13 Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.
#frase = input("digite uma frase: ")
#print(frase.strip())

# 14 Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.
#data = input("Digite uma data: ")
#dia, mes, ano = data.split("/")
#print(f"Dia: {dia}")
#print(f"Mes: {mes}")
#print(f"Ano: {ano}")

# 15 Escreva um programa que concatene duas strings fornecidas pelo usuário.
#str1 = input("digite o primeiro texto: ")
#str2 = input("digite o segundo texto: ")
#print(str1+str2)


# 16 Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas
#v1 = bool(input("Digite verdadeiro ou falso"))
#v2 = bool(input("Digite novamente: "))
#rs = v1 and v2
#print(f"O resultado entre: {v1} AND {v2} é igual a: {rs}")

# 17 Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.
#v1 = bool(input("Digite verdadeiro ou falso"))
#v2 = bool(input("Digite novamente: "))
#rs = v1 or v2
#print(f"O resultado entre: {v1} AND {v2} é igual a: {rs}")


# 18 Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.
#v1 = True
#v2 = False
#resultado_not = not v2
#print(resultado_not)

# 19 Faça um programa que compare se dois números fornecidos pelo usuário são iguais.
#num1 = int(input("Digite o primeiro número: "))
#num2 = int(input("Digite o segundo número: "))
#resultado = (num1 == num2)
#print(resultado)

# 10 Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
resultado = (num1 != num2)
print(resultado)