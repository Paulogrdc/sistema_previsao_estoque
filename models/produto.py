

class Produto: 
    def __init__(self, nome:str, id:int, preco:float, categoria:str, estoque_min:int ):
        self.nome_produto = nome
        self._id = id # -> fazer um property aqui 
        self.preco = preco
        self.categotria = categoria
        self._estoque_min = estoque_min # -> fazer um porperty aqui 


    