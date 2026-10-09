from repositories.produto_repository import Produtorepository


class Movimentacaorepository: 

    def registrar_movimentacao(self,movimentacao,conn):
        cur = conn.cursor()

        cur.execute("INSERT INTO MOVIMENTACAO (data, produto_id, quantidade, tipo_movimentacao) " \
        "VALUES (%s,%s,%s,%s)",  
        (movimentacao.data, movimentacao.produto, movimentacao.quantidade, movimentacao.tipo_movimentacao))


    def buscar_movimentacao(self,conn, movimentacao_produto): 
        repository_produto = Produtorepository()
        produto = repository_produto.buscar_produto(movimentacao_produto)
        produto_id = produto[0] 

        cur =  conn.cursor()

        cur.execute("SELECT * FROM MOVIMENTACAO WHERE produto_id = %s;", (produto_id,))
        
        historico = cur.fetchall()
        return historico 
