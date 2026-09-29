from services.movimentacao_Service import MovimentacaoService
from models.estoque import Estoque 
from models.movimentacao import Movimentacao 
from functionality.functions import Criar_produtos, verificar_tipo_trasacao



#produtos = Criar_produtos()


estoque = Estoque(2,2, 10)

movimentacao = Movimentacao("29/09/2026",2, 5, "Compra")


service_mv = MovimentacaoService()
service_mv.registrar_entrada(estoque, movimentacao)






