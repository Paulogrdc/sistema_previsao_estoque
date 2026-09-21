from models.produto import p1 
from rich import inspect

class Movimentacao: 
    def __init__(self, id:int, data:str , produto:object , quantidade:int, tipo_movimentacao:str ):
        self._id = id 
        
        self.data = data 
        self.produto = produto 
        self.quantidade= quantidade 
        self.tipo_movimentacao = tipo_movimentacao


    @property
    def id(self): 
        return self._id

    @id.setter
    def id(self,valor): 
        if valor <= 0: 
            raise ValueError("Valor invalido! ")
        else: 
            self._populacao = valor






