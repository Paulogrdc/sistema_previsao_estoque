from repositories.estoque_repository import Estoquerepository
from repositories.movimentacao_repository import Movimentacaorepository
from database import conectar

class MovimentacaoService: 


    def registrar_entrada(self, estoque, movimentacao):
        #1. Cria a conexão com o banco
        conn = conectar()

        try: 
            #2. Recebe uma movimentação e o estoque atraves de paramentros. 
        
            #3. Chama o estoque.receber_produto(quantidade)
            estoque.receber_produto(movimentacao.quantidade)

            #4. Atualizar o estoque no banco
            est_r = Estoquerepository()
            est_r.atualizar_estoque(estoque,conn)

            #5. Registrar a movimentação no banco
            mov_r = Movimentacaorepository()
            mov_r.registrar_movimentacao(movimentacao,conn)

            #6 commita a trasação 
            conn.commit()

            #7. Confirmar a operação
            print("Operação confirmada com sucesso!")

        except Exception as erro: 
            print(f"A operação falhou! O seu erro é de {erro}")
            conn.rollback()

        finally: 
            #8.fecha a operação
            conn.close()

        


    def registrar_saida(self, estoque, movimentacao): 
        #1. Cria a conexão com o banco
        conn = conectar()

        try: 
            #2. Receber uma movimentação e um estoque através de parâmetros. 

            #3. Chamar estoque.retirar_produto(quantidade)
            estoque.retirar_produto(movimentacao.quantidade)

            #4. Atualiza o estoque no banco
            est_r = Estoquerepository()
            est_r.atualizar_estoque(estoque,conn)

            #5. Registra a movimentação no banco
            mov_r = Movimentacaorepository()
            mov_r.registrar_movimentacao(movimentacao,conn)

            #6 commita a transação
            conn.commit()

            #7. Confirmar a operação
            print("Operação confirmada com sucesso!")

        except Exception as erro: 
            print(f"A Operação falhou! O seu erro é de {erro}")
            conn.rollback()

        finally:     
            #8. fecha a operação
            conn.close()

