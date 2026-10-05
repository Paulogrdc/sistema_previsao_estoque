from models.produto import Produto 
from repositories.produto_repository import Produtorepository
from services.movimentacao_Service import MovimentacaoService



def catalago():
    print("1-Adicionar Novo Produto ")
    print("2-Consultar Produto")
    print("3-Adicionar Movimentação")
    print("4-Sair do catalago")

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
    catalago()
    opcao = int(input("Escolha uma opção: "))
    while True: 
        match opcao:

            case 1: 
                try: 
                    produto = add_Novo_Produto()
                    repository_produto = Produtorepository()
                    repository_produto.cadastrar_produto(produto)
                    catalago()
                    opcao = int(input("Escolha uma opção: "))
                except Exception as erro: 
                    ja_existe_produto = erro
                    if ja_existe_produto:
                        print("Error! Já Existe um Produto com esse ID.")
                    else: 
                        print("ops! Algo deu errado.")

            case 2: 
                pass 
            case 3: 
                pass
            case 4: 
                break
                



def verificar_tipo_trasacao(movimentacao, service_mv):  
    if movimentacao.tipo_movimentacao == "Venda": 
        service_mv.registrar_saida(movimentacao)
    else: 
        service_mv.registrar_entrada(movimentacao)
