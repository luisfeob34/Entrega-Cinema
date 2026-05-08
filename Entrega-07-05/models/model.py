class Filme:
    def __init__(self, id, titulo, duracao):
        self.id = id
        self.titulo = titulo
        self.duracao = duracao

class Sessao:
    def __init__(self, id, horario, publico_atual, id_filme):
        self.id = id
        self.horario = horario
        self.publico_atual = publico_atual
        self.id_filme = id_filme