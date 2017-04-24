##entrada de dados
salario = input()
salario = float(salario)

##seleção
if(salario >= 0.00 and salario <= 2000.00):
    print ("Isento")

elif(salario >= 2000.01 and salario <= 3000.00):
    salario_base_calculo = salario - 2000
    imposto = (salario_base_calculo * 8) / 100
    print ("R$ %.2f" % imposto)

elif(salario >= 3000.01 and salario <= 4500.00):
    salario_base_calculo = salario - 3000
    imposto = (salario_base_calculo * 18) / 100 + (1000 * 8) / 100
    print ("R$ %.2f" % imposto)

else:
    salario_base_calculo = salario - 4500
    imposto = (salario_base_calculo * 28) / 100 + (1500 * 18) / 100 + (1000 * 8) / 100
    print ("R$ %.2f" % imposto)
