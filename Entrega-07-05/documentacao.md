# Documentação do Sistema - Rede de Cinemas

## 1. Requisitos Funcionais (RF)
* **RF01:** Cadastrar Filmes, Cinemas, Salas e Sessões.
* **RF02:** Registrar público total por sessão.
* **RF02:** Gerenciar salas e sessões (vincular filme, horário e cinema).
* **RF02:** Gerar relatórios de público por filme e por unidade.

## 2. Requisitos Não Funcionais (RNF)
* **RNF01 (Usabilidade):** O sistema deve possuir uma interface de linha de comando (CLI) intuitiva, com mensagens claras de erro e sucesso.
* **RNF02 (Confiabilidade):** Os dados devem ser persistidos em um banco de dados SQLite para garantir que as informações não sejam perdidas ao fechar o programa.
* **RNF03 (Desempenho):** As consultas de listagem de filmes e sessões devem ser processadas em menos de 2 segundos.
* **RNF04 (Portabilidade):** O sistema deve ser executável em qualquer sistema operacional que possua o interpretador Python 3.x instalado.
* **RNF05 (Manutenibilidade):** O código deve seguir a arquitetura em camadas (MVC + Service + Repository) para facilitar futuras manutenções e evoluções.

## 3. Regras de Negócio
* **RN01:** Não permitir sessões sobrepostas na mesma sala.
* **RN02:** O público não pode exceder a capacidade da sala.
* **RN03:** O sistema deve impedir a exclusão de filmes que possuam sessões ativas.
