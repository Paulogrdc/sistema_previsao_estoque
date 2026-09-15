

class Produto: 
    def __init__(self, nome:str, id:int, preco:float, categoria:str, estoque_min:int ):
        self.nome_produto = nome
        self._id = id # -> fazer um property aqui 
        self.preco = preco
        self.categotria = categoria
        self._estoque_min = estoque_min # -> fazer um porperty aqui 


    @property
    def id(self):
        return self._id 

    @id.setter
    def id(self,valor): 
        if valor <= 0: 
            raise ValueError("Valor invalido! ")
        else: 
            self._populacao = valor

    @property
    def estoque_min(self):
        return self._estoque_min 

    @estoque_min.setter
    def estoque_min(self,valor): 
        pass    # Para fazer esse property, eu preciso fazer uma analise de vendas do porduto