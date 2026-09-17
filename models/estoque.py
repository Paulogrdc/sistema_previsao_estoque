from models.produto import Produto 
from rich import inspect

class Estoque: 
    def __init__(self, id:int = 1 , produto:object = Produto, quantidade:int = 1 ):
         self.produto = produto
         self._id=  id  
         self._quantidade = None 

         self.quantidade = quantidade

    @property 
    def id(self): 
        return self._id 

    @id.setter
    def id(self, valor): 
          if valor < 0: 
               raise ValueError("Valor invalido! ")
          else: 
               self._populacao = valor


    @property
    def quantidade(self):
         return self._quantidade 

    @quantidade.setter
    def quantidade(self,valor): 
         if valor < 0: 
              print("Valor invalido! O estoque não pode ser negativo. ")
         else: 
              self._quantidade = valor  


    def receber_produto(self, quant):
         self.quantidade += quant
         return self.quantidade

    def retirar_produto(self,quant):
          self.quantidade -= quant
          return self.quantidade
         

    def ind_estoque_baixo(self):
         pass




