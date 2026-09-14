

class Estoque: 
    def __init__(self, produto:object, id:int , quantidade:int):
         self.produto = produto
         self._id=  id  # -> fazer um property aqui 
         self.quantidade = quantidade # -> fazer um property aqui 


    def receber_produto(self, quant):
         pass

    def retirar_produto(self,quant):
         pass 

    def ind_estoque_baixo(self):
         pass