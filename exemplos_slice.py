# Exemplos de utilização do Slice

texto = "python"
print(texto[0:3])

texto = "python"
print(texto[0])


texto = "python"
print(texto[0:5])


#Exemplos sem o início

texto = "python"
print(texto[:4])


texto = "python"
print(texto[2:])



# SEQUENCIA -> [início:fim:passo]

texto = "python"
print(texto[::2])

# TABELA PARA MEMORIZAR 

#[:]     -> tudo
#[::1]   -> normal
#[::2]   -> pula de 2 em 2
#[::-1]  -> invertido
#[::-2]  -> invertido pulando


# INVERTER TUDO 
texto = "python"
print(texto[::-1])


#Exemplos para inverter uma lista 
lista = [1,2,3,4,5]
print(lista[::-1])

