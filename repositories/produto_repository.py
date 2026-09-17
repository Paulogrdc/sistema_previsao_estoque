from database import conectar
from models.produto import P2

class Produtorepository: 

    def cadastrar_produto(self,produto):
        conn = conectar()
        cur = conn.cursor()

        cur.execute("INSERT INTO PRODUTO (id, nome_produto, preco, categoria, estoque_min)" \
        " VALUES (%s,%s,%s,%s,%s)", 
        (produto.id, produto.nome_produto, produto.preco, produto.categoria, produto.estoque_min))

        conn.commit()




        
