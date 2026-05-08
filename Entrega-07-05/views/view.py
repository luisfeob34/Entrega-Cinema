class CinemaView:
    def exibir_menu(self):
        print("\n" + "="*30)
        print("   REDE DE CINEMAS - VIEW")
        print("="*30)
        print("1. Cadastrar Novo Filme")
        print("2. Listar Filmes")
        print("0. Sair")
        return input("\nEscolha uma opção: ")

    def solicitar_dados_filme(self):
        titulo = input("Título do Filme: ")
        duracao = input("Duração (min): ")
        return titulo, duracao

    def mostrar_mensagem(self, mensagem):
        print(f"-> {mensagem}")

    def listar_filmes(self, filmes):
        print("\n--- FILMES EM CARTAZ ---")
        if not filmes:
            print("Nenhum filme cadastrado.")
        for f in filmes:
            print(f"ID: {f[0]} | Título: {f[1]} | Duração: {f[2]} min")