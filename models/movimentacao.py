

class Movimentacao: 
    def __init__(self, id: int, data:int, produto:str, quantidade:int, tipo_movimentacao:str):
        self._id = id # -> fazer um property aqui 
        self.data = data 
        self.produto = produto 
        self.quantidade= quantidade 
        self.tipo_movimentacao = tipo_movimentacao