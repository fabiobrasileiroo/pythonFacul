list = [1,3,5,2,4,6,8,19]

print(len(list))
for i,value in enumerate(list):
  if(value % 6 ==0):
    print(f"Numeros multiplos de 6: {value}[{i}]")


