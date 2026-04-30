#O programa deve começar solicitando ao usuário que insira seu nome.
nome = input("Qual o seu nome:")
print(nome)
#Em seguida, o programa deve pedir ao usuário para inserir o valor do seu salário. Considere que este valor pode ser um número decimal.
salario = float(input("Qual o valor do seu salario: "))
print(salario)
#Depois, o programa deve solicitar a porcentagem do bônus recebido pelo usuário, que também pode ser um número decimal.
bonus = float(input("Qual foi o seu bonus: "))
print(bonus)
#O cálculo do KPI do bônus de 2024 é de 1000 + salario * bônus
kpi_bonus = (1000 + (salario * bonus))  
print(kpi_bonus)
#Finalmente, o programa deve imprimir uma mensagem no seguinte formato: "Olá [nome], o seu valor bônus foi de 5000".
#Exemplo de Saída:
#Se o usuário digitar "Luciano" como nome, "5000" como salário e "1.5" como bônus, o programa deve imprimir: