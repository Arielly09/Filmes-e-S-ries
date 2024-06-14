class Filme(Programa    ):
    def __init__(self, nome, ano, duracao):
        self.__nome = nome.title()
        self.ano = ano
        self.duracao = duracao
        self.__likes = 0

class Serie(Programa):
    def __init__(self, nome, ano, temporada):
        self.__nome = nome
        self.ano = ano
        self.temporada = temporada 
        self.__likes = 0
      
vingadores = Filme('Vingadores - Guerra Infinita', 2018, 160)
vingadores.dar_likes()
print(f'Nome: {vingadores.nome} - Ano: {vingadores.ano} - Duração: {vingadores.duracao} - Likes: {vingadores.likes}')


atlanta = Serie('Atlanta', 218, 2)
atlanta.dar_likes()
atlanta.dar_likes()

print(f'Nome: {atlanta.nome} - Ano: {atlanta.ano} - Temporadas: {atlanta.Temporadas}')

def dar_likes(self):
        self.likes += 1
