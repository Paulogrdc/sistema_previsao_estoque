from services.movimentacao_Service import MovimentacaoService
from models.estoque import Estoque 
from repositories.estoque_repository import Estoquerepository
from models.movimentacao import Movimentacao 
from functionality.functions import Criar_produtos, verificar_tipo_trasacao
from database import conectar 


 
#produtos = Criar_produtos()

conn = conectar()

movimentacao = Movimentacao("01/10/2026", 2, 5 , "Compra")

reposy_estoque = Estoquerepository()
estoque = reposy_estoque.buscar_estoque(2, conn)
print(estoque.quantidade)

#estoque = Estoque(2,2, 10)
#verificar_tipo_trasacao(movimentacao, estoque, MovimentacaoService())






