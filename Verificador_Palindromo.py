'''
Exercício 22: Verificador de Palíndromo
Crie um programa que verifica se uma palavra ou frase é um palíndromo (lê-se igualmente de trás para frente, 
desconsiderando espaços e pontuações). Utilize try-except para garantir que a entrada seja uma string. 

Dica: Utilize a função isinstance() para verificar o tipo da entrada.
'''

entrada = "Ovo"       #Variavel 
if isinstance(entrada, str):   #verificando se a minha variável de "entrada" é uma string
    formatado = entrada.replace(" ", "").lower() # se for uma string vai fazer um replace ou seja substituir " " por """ .lower -> Vai romover os campo vazios e deixar tudo minuscula.
    if formatado == formatado[::-1]: #fazendo um fatiamento de sequnencia, em ingles Slice ou Slicing
        print("É um palíndromo.")
    else:
        print("Não é um palíndromo.")
else:
    print("Entrada inválida. Por favor, digite uma palavra ou frase.")

