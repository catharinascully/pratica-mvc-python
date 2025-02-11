from database import Database

class Tarefa:
    def __init__(self, id, titulo, data_conclusao):
        self.id = id
        self.titulo = titulo
        self.data_conclusao = data_conclusao

    def salvarTarefa(self):
        """Salva uma nova tarefa no banco de dados."""
        db = Database()
        db.conectar()

        sql = 'INSERT INTO tarefa (titulo, data_conclusao) VALUES (%s, %s)' 
        params = (self.titulo, self.data_conclusao)
        db.executar(sql, params)
        db.desconectar()
    
    def listarTarefas(self):
        """Retorna uma lista com todas as tarefas cadastradas."""
        db = Database()
        db.conectar()

        sql = 'SELECT id, titulo, data_conclusao FROM tarefa'
        tarefas = db.consultar(sql)
        db.desconectar()
        return tarefas if tarefas else []
    
    def apagarTarefa(self):
        """Apaga uma tarefa cadastrada no banco de dados."""
        db = Database()
        db.conectar()

        sql = 'DELETE FROM tarefa WHERE id = %s'
        params = (self.id,) # Precisa passar como tupla?
        db.executar(sql, params)
        db.desconectar()