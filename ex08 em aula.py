salario_atual = int(input("Escreva seu salário atual: "))
aumento = int(input("Escreva a porcentagem de aumento: "))
res = salario_atual*((aumento/100))+salario_atual
print("Seu salário atual é ", salario_atual, "após o aumento de ", aumento,"%", "seu salário será de R$", res)