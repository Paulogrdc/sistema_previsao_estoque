
class Estoquerepository:  


    def atualizar_estoque(self, estoque, conn):

        cur = conn.cursor()

        cur.execute("UPDATE ESTOQUE SET quantidade = %s "\
        "where produto_id = %s",
        (estoque.quantidade, estoque.produto))
