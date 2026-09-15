

class Movimentacao: 
    def __init__(self, id: int, data:int, produto:str, quantidade:int, tipo_movimentacao:str):
        self._id = id # -> fazer um property aqui 
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