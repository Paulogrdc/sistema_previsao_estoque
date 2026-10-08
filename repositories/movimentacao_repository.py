
class Movimentacaorepository: 

    def registrar_movimentacao(self,movimentacao,conn):
        cur = conn.cursor()

        cur.execute("INSERT INTO MOVIMENTACAO (data, produto_id, quantidade, tipo_movimentacao) " \
        "VALUES (%s,%s,%s,%s)",  
        (movimentacao.data, movimentacao.produto, movimentacao.quantidade, movimentacao.tipo_movimentacao))


    def buscar_historico(self,conn): 
        cur =  conn.cursor()

        cur.execute("SELECT * FROM MOVIMENTACAO;")
        historico = cur.fetchone()

        return historico 
