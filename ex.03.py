salario = float(input("Informe o salário: "))
aumento = float(input("informe o percentual aumento: "))

result = salario * aumento
total = (result / 100)  + salario

print("O salário atualizado é: ", total)