list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# for value,i in enumerate(list):
#   if(i>0 and i <9 ):
#     print(f"Valor: {value} - index: {i}")
somaIntervalo = 0
for value in list:
  if(value > 0 and value <=9):
    print(f"A: Intervalo: {value}")
    somaIntervalo+=value
  
  if(value >7 and value <=12):
    print(f"B: Intervalo: {value}")
    somaIntervalo+=float(value)
  

  
  if(value % 2 == 0):
    print(f"Par: {value}")
  else:
    print(f"Impar: {value}")

print(f"Soma de dois intervalos:{somaIntervalo}")
  

list.reverse()
for value in list:
  print(f"Reverter: {value}")

