from database import conectar 


class Movimentacaorepository: 

    def registar_movimentacao(self,movimentacao):
        conn = conectar()
        cur = conn.cursor()

        cur.execute("INSERT INTO MOVIMENTACAO (data, produto_id, quantidade, tipo_movimentacao) " \
        "VALUES (%s,%s,%s,%s)",  
        (movimentacao.data, movimentacao.produto, movimentacao.quantidade, movimentacao.tipo_movimentacao))

        conn.commit() 

        cur.close()
        conn.close()
