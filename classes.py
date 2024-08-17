class Cliente():
    
    def __init__(self, nome, senha, cpf, telefone, idade, saldo ):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.telefone = telefone
        self.senha = senha
        self.saldo = saldo
        self.carrinho = []


class Produto():
    nome:str
    preco:float
    quantidade:int
    
    def __init__(self, nome, quantidade, preco):
        self.nome = nome
        self.quantidade = quantidade
        self.preco = preco


class Adiministrador():
    nome: str
    matricula: int
    senha: str
 
    def __init__ (self,nome, matricula, senha ):
        self.nome= nome
        self.matricula=matricula
        self.senha= senha
 
