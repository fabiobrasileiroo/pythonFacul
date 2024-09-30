try:
    salario_valor = float(input("Digite o valor do salário atual: "))
    porcentagem_aumento = float(input("Digite a porcentagem de aumento: "))

    if salario_valor < 0 or porcentagem_aumento < 0:
        print("Valor do salário e porcentagem de aumento devem ser positivos.")
    else:
        aumento = (salario_valor * porcentagem_aumento) / 100
        novo_salario = salario_valor + aumento

        print(f"Valor do aumento: R$ {aumento:.2f}")
        print("Valor do aumento: R$ %.2f"%aumento)
        print(f"Novo salário: R$ {novo_salario:.2f}")

except ValueError:
    print("Por favor, digite apenas números válidos.")
