from services.movimentacao_Service import MovimentacaoService
from models.estoque import Estoque 
from models.movimentacao import Movimentacao 
from functionality.functions import Criar_produtos



produtos = Criar_produtos()


estoque = Estoque(2,produtos.id, 10)




