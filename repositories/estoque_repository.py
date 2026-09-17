from database import conectar 
from models.estoque import est2

class Estoquerepository:  


    def registrar_estoque(self, estoque):

        conn = conectar()
        cur = conn.cursor()

        cur.execute("INSERT INTO ESTOQUE (id, produto_id, quantidade) " \
        "VALUES (%s,%s,%s)", (estoque.id, estoque.produto, estoque.quantidade))

        conn.commit()

        cur.close()
        conn.close()

