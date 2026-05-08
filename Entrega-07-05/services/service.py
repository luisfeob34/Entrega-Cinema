from models.model import Filme
from repository.repository import CinemaRepository

class CinemaService:
    def __init__(self):
        self.repo = CinemaRepository()

    def validar_e_cadastrar_filme(self, titulo, duracao):
        # REGRA DE NEGÓCIO: Título não pode ser vazio e duração > 30min
        if not titulo.strip():
            raise ValueError("O título não pode estar vazio.")
        if duracao < 30:
            raise ValueError("Filmes devem ter pelo menos 30 minutos.")
        
        novo_filme = Filme(None, titulo, duracao)
        self.repo.salvar_filme(novo_filme)
        return f"Filme '{titulo}' cadastrado com sucesso!"