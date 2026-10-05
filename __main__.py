from services.movimentacao_Service import MovimentacaoService
from models.estoque import Estoque 
from repositories.estoque_repository import Estoquerepository
from models.movimentacao import Movimentacao 
from functionality.functions import Criar_produtos, verificar_tipo_trasacao






#produtos = Criar_produtos()

movimentacao = Movimentacao("05/10/2026", 1, 1, "Venda")
verificar_tipo_trasacao(movimentacao, MovimentacaoService())






