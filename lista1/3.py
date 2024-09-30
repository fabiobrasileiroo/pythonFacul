listName = []

for i in range(10):
  name = int(input())
  listName.append(name)


for  i,value in enumerate(listName):
  if(value % 2 == 0):
    print(f"Par:{value} - Index: {i+1}")
  else:
    print(f"Impar:{value} - Index: {i+1}")