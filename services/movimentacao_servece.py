from models.produto import Produto
from models.estoque import Estoque 
from models.movimentacao import Movimentacao

from repositories.produto_repository import Produtorepository
from repositories.estoque_repository import Estoquerepository
from repositories.movimentacao_repository import Movimentacaorepository


# Cadastra o produto
p1 = Produto("monitor", 1,  1034.22, "periferico", 20)
#pro_r = Produtorepository()
#pro_r.cadastrar_produto(p1)



class Movimentacaoservece: 


    def registrar_entrada(self): 
        #1. Receber uma movimentação
        mv1 = Movimentacao(1, "21/09/2026", p1.id, 30, "Compra")

        #2. Identificar que é uma entrada
        #3. Buscar o estoque relacionado ao produto
        est_p1 = Estoque(1, p1.id, 30) 

        #4. Chamar estoque.receber_produto(quantidade)
        est_p1.receber_produto(est_p1.quantidade)

        #5. Atualizar o estoque no banco
        est_r = Estoquerepository()
        est_r.atualizar_estoque(est_p1)

        #6. Registrar a movimentação no banco
        mov_r = Movimentacaorepository()
        mov_r.registar_movimentacao(mv1)

        #7. Confirmar a operação
        print("Operação confirmada com sucesso! ")


    def registrar_saida(self): 
        #1. Receber uma movimentação
        mv2 = Movimentacao(2, "21/09/2026", p1.id, 2, "venda")

        #2. Identificar que é uma entrada
        #3. Buscar o estoque relacionado ao produto
        est_p1 = Estoque(1, p1.id, 30) 

        #4. Chamar estoque.retirar_produto(quantidade)
        est_p1.retirar_produto(2)

        #5. Atualizar o estoque no banco
        est_r = Estoquerepository()
        est_r.atualizar_estoque(est_p1)

        #6. Registrar a movimentação no banco
        mov_r = Movimentacaorepository()
        mov_r.registar_movimentacao(mv2)

        #7. Confirmar a operação
        print("Operação confirmada com sucesso! ")




movi_servece = Movimentacaoservece()

movi_servece.registrar_saida()