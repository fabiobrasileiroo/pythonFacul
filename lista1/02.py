listName = []

for i in range(10):
  name = input()
  listName.append(name)


for value, i in enumerate(listName):
  print(f"Nomes:{value} - Index: {i+1}")