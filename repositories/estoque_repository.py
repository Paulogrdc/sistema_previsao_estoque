from models.estoque import Estoque 


class Estoquerepository:  


    def atualizar_estoque(self, estoque, conn):

        cur = conn.cursor()

        cur.execute("UPDATE ESTOQUE SET quantidade = %s "\
        "where produto_id = %s",
        (estoque.quantidade, estoque.produto))


    def buscar_estoque(self, produto_id, conn): 

        cur = conn.cursor()

        #busca o estoque do produto
        cur.execute("SELECT id, produto_id, quantidade " \
        "FROM ESTOQUE " \
        "WHERE produto_id = %s", 
        (produto_id,))

        #Retorna as linhas do estoque do produto
        rows = list(cur.fetchone())

        if rows != None: 
            estoque = Estoque(rows[0], rows[1], rows[2])
            return estoque 
        else: 
            return None
        

