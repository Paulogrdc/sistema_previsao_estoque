from models.produto import Produto 
from repositories.produto_repository import Produtorepository


def Criar_produtos():
    nome = input("Insira o nome do produto: ")
    id = int(input("Insira um id para o produto: "))
    preco = float(input("Insira o preço do produto: "))
    categoria = input("Qual a categoria do produto? ")
    est_min = int(input("Qual o estoque minimo do Produto? ")) 

    p = Produto(nome, id, preco, categoria, est_min)

    Produto_repo = Produtorepository()
    Produto_repo.cadastrar_produto(p)

    return p 





