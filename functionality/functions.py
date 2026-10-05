from models.produto import Produto 
from repositories.produto_repository import Produtorepository
from services.movimentacao_Service import MovimentacaoService


def add_Novo_Produto():
    nome = input("Digite o nome do Produto: ")
    id = int(input("Digite um ID para o produto: "))
    preco = float(input("Digite o preço do produto: "))
    categoria = input("Digite a categoria do produto: ")
    est_min = int(input("Digite um estoque mínimo para o Proiduto: "))

    produto = Produto(nome, id, preco, categoria, est_min)
    return produto 

    # Você não pode adicionar um produto Repetido

def consultar_Produto(): 
    pass

def add_Movimnentacao(): 
    pass 

def menu(): 
    pass 


def verificar_tipo_trasacao(movimentacao, service_mv):  
    if movimentacao.tipo_movimentacao == "Venda": 
        service_mv.registrar_saida(movimentacao)
    else: 
        service_mv.registrar_entrada(movimentacao)
