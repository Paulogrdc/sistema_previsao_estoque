from database import conectar 


class Movimentacaorepository: 

    def registrar_movimentacao(self,movimentacao,conn):
        cur = conn.cursor()

        cur.execute("INSERT INTO MOVIMENTACAO (data, produto_id, quantidade, tipo_movimentacao) " \
        "VALUES (%s,%s,%s,%s)",  
        (movimentacao.data, movimentacao.produto, movimentacao.quantidade, movimentacao.tipo_movimentacao))

        cur.close()
