class Filme:
    def __init__(self, nome, ano, duracao):
        self.nome = nome.title()
        self.ano = ano
        self.duracao = duracao
        self.likes = 0

        def dar_like(self):
            self.likes += 1

class Serie:
    def __init__(self, nome, ano, temporada):
        self.nome = nome
        self.ano = ano
        self.temporada = temporada 
        self.likes = 0

    def dar_likes(self):
        self.likes += 1

vingadores = Filme('Vingadores - Guerra Infinita', 2018, 160)
print(f'Nome: {vingadores.nome} - Ano: {vingadores.ano} - Duração: {vingadores.duracao} - Likes: {vingadores.likes}')

atlanta = Serie('Atlanta', 218, 2)

print(f'Nome: {atlanta.nome} - Ano: {atlanta.ano} - Temporadas: {atlanta.Temporadas}')

atlanta = Serie('atlanta', 2018, 2)
