from repositories.produto_repository import Produtorepository
from repositories.estoque_repository import Estoquerepository
from repositories.movimentacao_repository import Movimentacaorepository

class Movimentacaoservece: 


    def registrar_entrada(self, estoque, movimentacao): 
        #1. Receber uma movimentação
        #2. Identificar que é uma entrada
        #3. Buscar o estoque relacionado ao produto
    
        #4. Chamar estoque.receber_produto(quantidade)
        estoque.receber_produto(movimentacao.quantidade)

        #5. Atualizar o estoque no banco
        est_r = Estoquerepository()
        est_r.atualizar_estoque(estoque)

        #6. Registrar a movimentação no banco
        mov_r = Movimentacaorepository()
        mov_r.registar_movimentacao(movimentacao)
        
        #7. Confirmar a operação
        print("Operação confirmada com sucesso! ")


    def registrar_saida(self, estoque, movimentacao): 
        #1. Receber uma movimentação
        #2. Identificar que é uma saida
        #3. Buscar o estoque relacionado ao produto 

        #4. Chamar estoque.retirar_produto(quantidade)
        estoque.retirar_produto(movimentacao.quantidade)

        #5. Atualizar o estoque no banco
        est_r = Estoquerepository()
        est_r.atualizar_estoque(estoque)

        #6. Registrar a movimentação no banco
        mov_r = Movimentacaorepository()
        mov_r.registar_movimentacao(movimentacao)

        #7. Confirmar a operação
        print("Operação confirmada com sucesso! ")
