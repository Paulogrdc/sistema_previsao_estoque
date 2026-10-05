from repositories.estoque_repository import Estoquerepository
from repositories.movimentacao_repository import Movimentacaorepository
from database import conectar

class MovimentacaoService: 


    def registrar_entrada(self,movimentacao):
        #1. Cria a conexão com o banco
        conn = conectar()

        try: 
            #2.Receber uma movimentação atraves de paramentro. 
        
            #3 buscar o estoque 
            est_r = Estoquerepository()
            estoque = est_r.buscar_estoque(movimentacao.produto,conn)

            #4. Chamar o estoque.receber_produto(quantidade)
            estoque.receber_produto(movimentacao.quantidade)

            #5. Atualizar o estoque no banco
            est_r.atualizar_estoque(estoque, conn)

            #6. Registrar a movimentação no banco
            mov_r = Movimentacaorepository()
            mov_r.registrar_movimentacao(movimentacao,conn)   

            #7 commitar a trasação 
            conn.commit()

            #8. Confirmar a operação
            print("Operação confirmada com sucesso!")

        except Exception as erro: 
            print(f"A operação falhou! O seu erro é de {erro}")
            conn.rollback()

        finally: 
            #9.fechar a operação
            conn.close()

        

    def registrar_saida(self, movimentacao): 
        #1. Criar a conexão com o banco
        conn = conectar()

        try: 
            #2.Receber uma movimentação atraves de paramentro. 

            #3 buscar o estoque 
            est_r = Estoquerepository()
            estoque = est_r.buscar_estoque(movimentacao.produto,conn)

            #4 Atualizar o estoque em memória
            estoque.retirar_produto(movimentacao.quantidade)

            #5. Atualizar o estoque no banco
            est_r.atualizar_estoque(estoque,conn)

            #6. Registrar a movimentação no banco
            mov_r = Movimentacaorepository()
            mov_r.registrar_movimentacao(movimentacao,conn)

            #7 commitar a transação
            conn.commit()

            #8. Confirmar a operação
            print("Operação confirmada com sucesso!")

        except Exception as erro: 
            print(f"A Operação falhou! O seu erro é de {erro}")
            conn.rollback()

        finally:     
            #9. fechar a operação
            pass
