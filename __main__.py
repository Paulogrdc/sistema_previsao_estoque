from services.movimentacao_servece import Movimentacaoservece
from repositories.produto_repository import Produtorepository
from models.produto import Produto
from models.estoque import Estoque 
from models.movimentacao import Movimentacao 


# inserir Produto 
p1 = Produto("fone", 1, 100, "Periferico", 20)
#p1_reposy = Produtorepository()
#p1_reposy.cadastrar_produto(p1)


est_p1 = Estoque(1, p1.id, 10) 
mv_p1 = Movimentacao("12/08/2026",p1.id,2,"Venda")

mvm_servece = Movimentacaoservece()
mvm_servece.registrar_saida(est_p1,mv_p1)

