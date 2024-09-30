notas= []
for notas in range(5):
  nota = float(input(f"Digite a nota {notas+1}: "))
  notas.append(notas)
for nota in notas:
  print(nota)

