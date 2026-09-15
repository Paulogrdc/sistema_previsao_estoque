

class Estoque: 
    def __init__(self, produto:object, id:int , quantidade:int):
         self.produto = produto
         self._id=  id  # -> fazer um property aqui 
         self.quantidade = quantidade # -> fazer um property aqui 


    @property 
    def id(self): 
        return self._id 

    @id.setter
    def id(self, valor): 
          if valor <= 0: 
               raise ValueError("Valor invalido! ")
          else: 
               self._populacao = valor

    @property
    def quantidade(self):
         if self.quantidade < 0: 
          print("Alerta! O valor do estoque não pode ser negativo!") 
        
    def receber_produto(self, quant):
         pass

    def retirar_produto(self,quant):
         pass 

    def ind_estoque_baixo(self):
         pass