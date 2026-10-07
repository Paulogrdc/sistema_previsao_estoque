from models.produto import Produto 
from repositories.produto_repository import Produtorepository
from models.movimentacao import Movimentacao
from services.movimentacao_Service import MovimentacaoService
from rich import print 
from rich.console import Console
from rich.table import Table 


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


def Consultar_Produto():
    nome_produto = input("Qual o Produdo você deseja consultar? ")

    repository_produto = Produtorepository()
    tabela_produto = repository_produto.buscar_produto(nome_produto)

    if tabela_produto != None: 
        caixa = Table(title="PRODUTO")
        caixa.add_column("ID")
        caixa.add_column("Nome")
        caixa.add_column("PRECO")
        caixa.add_column("CATEGORIA")
        caixa.add_column("ESTOQUE MÍNIMO")

        caixa.add_row(str(tabela_produto[0]),str(tabela_produto[1]), str(tabela_produto[2]), str(tabela_produto[3]), str(tabela_produto[4]))
        console = Console()
        console.print(caixa) 
    else: 
        print("Produto não localizado. ") 


def verificar_tipo_trasacao(movimentacao, mv_service):  
    if movimentacao.tipo_movimentacao == "Venda": 
        mv_service.registrar_saida(movimentacao)
    else: 
        mv_service.registrar_entrada(movimentacao)


def add_nova_Movimnentacao():
    data = input("Digite a data: ")
    produto = int(input("Digite o id do produto: "))
    quantidade = int(input("Digite a quantidade: "))
    tipo_movimentacao = input("Digite o tipo da movimentação: ")

    movimentacao = Movimentacao(data, produto, quantidade, tipo_movimentacao)
    return movimentacao



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
                        print("[/red]Error! Já Existe um Produto com esse ID.[]")
                    else: 
                        print("[/red] ops! Algo deu errado.[/]")

            case 2:
                Consultar_Produto()
                catalago()
                opcao = int(input("Escolha uma opção: "))

            case 3: 
                mv = add_nova_Movimnentacao()
                mv_service = MovimentacaoService()
                verificar_tipo_trasacao(mv, mv_service)
                catalago()
                opcao = int(input("Escolha uma opção: "))
                
            case 4: 
                break
                
