import sqlite3

class CinemaRepository:
    def __init__(self, db_name='cinema.db'):
        self.conn = sqlite3.connect(db_name)
        self._criar_tabelas()

    def _criar_tabelas(self):
        cursor = self.conn.cursor()
        # Tabela de Filmes
        cursor.execute('''CREATE TABLE IF NOT EXISTS filmes 
                          (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                           titulo TEXT, duracao INTEGER)''')
        # Tabela de Sessões
        cursor.execute('''CREATE TABLE IF NOT EXISTS sessoes 
                          (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                           horario TEXT, publico INTEGER, filme_id INTEGER,
                           FOREIGN KEY(filme_id) REFERENCES filmes(id))''')
        self.conn.commit()

    def salvar_filme(self, filme):
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO filmes (titulo, duracao) VALUES (?, ?)", 
                       (filme.titulo, filme.duracao))
        self.conn.commit()

    def listar_todos_filmes(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM filmes")
        return cursor.fetchall()