import mysql.connector # Importando a biblioteca do conector do MySQL
from mysql.connector import Error # Importando a classe Error para tratar as mensagens de erro do código
from dotenv import load_dotenv # Importando a função load_dotenv
from os import getenv # Importando a função getenv

class Database:
    def __init__(self):
        load_dotenv()
        self.host = getenv('DB_HOST')
        self.username = getenv('DB_USER')
        self.password = getenv('BD_PSWD')
        self.database = getenv('DB_DATABASE')
        self.connection = None # Inicialização da conexão
        self.cursor = None # Inicialização do cursor

    def conectar(self):
        """Estabelece uma conexão com o banco de dados."""

        try: 
            self.connection = mysql.connector.connect(
                host = self.host,
                database = self.database
            )