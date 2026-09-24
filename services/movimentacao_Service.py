from repositories.estoque_repository import Estoquerepository
from repositories.movimentacao_repository import Movimentacaorepository

class MovimentacaoService: 


    def registrar_entrada(self, estoque, movimentacao): 
        #1. Receber uma movimentação e um estoque atraves de paramentros. 
    
        #2. Chamar estoque.receber_produto(quantidade)
        estoque.receber_produto(movimentacao.quantidade)

        #3. Atualizar o estoque no banco
        est_r = Estoquerepository()
        est_r.atualizar_estoque(estoque)

        #4. Registrar a movimentação no banco
        mov_r = Movimentacaorepository()
        mov_r.registrar_movimentacao(movimentacao)

        #5. Confirmar a operação
        # criar uma função para isso


    def registrar_saida(self, estoque, movimentacao): 
        #1. Receber uma movimentação e um estoque atraves de paramentros. 

        #2. Chamar estoque.retirar_produto(quantidade)
        estoque.retirar_produto(movimentacao.quantidade)

        #3. Atualizar o estoque no banco
        est_r = Estoquerepository()
        est_r.atualizar_estoque(estoque)

        #4. Registrar a movimentação no banco
        mov_r = Movimentacaorepository()
        mov_r.registar_movimentacao(movimentacao)

        #5. Confirmar a operação
        # criar uma função para isso
