''''
nome = "Franci"
try:
    Qtd_caracteres = len(5)
    print(f"Minha quantidade de caracteres é: {Qtd_caracteres}")
except:
    print("Tem alguma coisa errada no seu código hein")
else: #aqui eu posso colocar um validação se o meu código rodar eu também posso fazer executar essa etapa 
    print("ok")
finally: # Também posso utilizar o finally -> independente do que aconte rode essa parte 
    print("vou rodar de qualquer jeito hein ")

'''


num1 = "Fran"
if isinstance(num1, int):
    print(f"A minha variável é um inteiro")
else:   
    print(f"A minha variável não é um inteiro")


