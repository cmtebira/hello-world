vendedor = input()
salario_fixo = float(input())
total_vendas_mes = float(input())
total_receber = salario_fixo + ((total_vendas_mes*15)/100)
print("TOTAL = R$ %.2f" % total_receber)
