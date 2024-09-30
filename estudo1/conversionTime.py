#segundos = int(input()) # tempo em segundo
# voltar o hora, minuto e segundo
#horas = segundos * 60 * 60
#minutos = (segundos * 60)

#print(f'{horas}:{minutos}:{segundos}')

class Pessoa:
  def __init__ (self, nome, sexo,cpf):
    self.nome = nome
    self.sexo = sexo
    self.cpf = cpf 

if __name__ == "__main__":
  pessoa1 = Pessoa("Joao","M","1234")
  print(pessoa1.nome)