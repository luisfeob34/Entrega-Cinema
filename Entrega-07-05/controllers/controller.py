from views.view import CinemaView
from services.service import CinemaService

class CinemaController:
    def __init__(self):
        self.view = CinemaView()
        self.service = CinemaService()

    def iniciar(self):
        while True:
            opcao = self.view.exibir_menu()
            
            if opcao == "1":
                self.processar_cadastro()
            elif opcao == "2":
                self.processar_listagem()
            elif opcao == "0":
                self.view.mostrar_mensagem("Encerrando sistema...")
                break
            else:
                self.view.mostrar_mensagem("Opção Inválida!")

    def processar_cadastro(self):
        titulo, duracao = self.view.solicitar_dados_filme()
        try:
            duracao_int = int(duracao)
            resultado = self.service.validar_e_cadastrar_filme(titulo, duracao_int)
            self.view.mostrar_mensagem(resultado)
        except ValueError as e:
            self.view.mostrar_mensagem(f"Erro de Validação: {e}")

    def processar_listagem(self):
        filmes = self.service.repo.listar_todos_filmes()
        self.view.listar_filmes(filmes)