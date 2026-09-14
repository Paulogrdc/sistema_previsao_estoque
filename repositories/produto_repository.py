from database import conectar

class Repositoryproduto: 
    conn = conectar()
    cur = conn.cursor()
    def cadastrar_produto(self,produto):
        pass
