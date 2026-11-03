from models.movimentacao import Movimentacao
from services.movimentacao_Service import MovimentacaoService
from functionality.functions import verificar_tipo_trasacao
import csv


with open("movimentacoes_historicas_3_anos.csv", "r", encoding="utf-8", newline='') as arquivo:

    for linha in csv.DictReader(arquivo):
        mv = Movimentacao(
            linha['data'], #data : str 
            int(linha['produto_id']), #produto_id : int
            int(linha['quantidade']), #quantidade: int
            linha['tipo_movimentacao'] #tipo_movimentacao: str
        )
        verificar_tipo_trasacao(mv, MovimentacaoService())



from database import conectar
import csv
conn = conectar()

with conn.cursor() as cur: 
    cur.execute("SELECT nome_produto from PRODUTO;")
    produtos = cur.fetchall()
    
with open("Produtos.csv", 'w+', encoding="utf-8", newline='') as arquivo:
    arquivo.write("nome_produto")
    char = ["(", ")"]
    for linha in arquivo:
        arquivo.write("\n")
        for c in char:
            if c in linha : 
                arquivo.write(str(linha).replace(c, " "))
            else:
                arquivo.write(str(linha))
            
