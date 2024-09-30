# valor metros 
# converte em milisegundos
dias = int(input())
horas = int(input())
minuto = int(input())
segundos = int(input())

dias_segundo = dias * 24 * 60 *60
horas_segundo = horas * 60 * 60
segundos_segundos = segundos  * 60
valorTotal = dias_segundo + horas_segundo * segundos
print("Dias normal", dias)
print("Dias segundo:",dias_segundo)
print("Horas segundo:",horas)
print("Horas segundo:",horas_segundo)
print("Segundo:",segundos)
print("Valor total em segundos:",valorTotal)






