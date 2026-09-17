from rich import inspect

class Produto: 
    def __init__(self, nome:str, id:int, preco:float, categoria:str, estoque_min:int = 0 ):
        self.nome_produto = nome
        self._id = id # -> fazer um property aqui 
        self.preco = preco
        self.categoria = categoria
        self._estoque_min = estoque_min


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
        if valor < 0: 
            print("valor invalido!")
        else: 
            self._estoque_min = valor  # Para fazer esse property, eu preciso fazer uma analise de vendas do porduto
 



