from classes import *
from previwer import *
import getpass
import time
import os

lista_carrinho=[]
lista_produtos=[]
lista_usuario=[]

#====================LISTAR=====================
def listar_produtos_admin(produtos):
    for i in range(len(produtos)):
        print(f"| {i + 1} | {produtos[i].nome} | {produtos[i].quantidade} | R$ {produtos[i].preco}    |")
    pressione_enter()

def listar_produstos(produtos, carrinho): #Listar produtos e Adc. no carrinho
    for i in range(len(produtos)):
        print(f"| {i + 1} | {produtos[i].nome} | {produtos[i].quantidade} | R$ {produtos[i].preco}    |")
    op = int(input("Escolha um produto: "))
    produto_selecionado = produtos[op - 1]
    carrinho.append(produto_selecionado)

def listar_usuarios_do_sistema(lista_usuarios): #Listar Usuarios para o admin
    print("      [USUÁRIOS CRIADOS]")
    print("+============================+")
    for _ in range(0,lista_usuarios):
        print(f"{lista_usuarios[_].nome}")
    print("+============================+")

def listar_carrinho(lista_carrinho, produto, usuario): #Visualizar Carrinho, Efetuar pagamento e Remover produto
    print("+==============[CARRINHO]==============+")
    for i in range(len(lista_carrinho)):
        print(f"{i + 1} - {produto[i].nome} | {produto[i].preco} | {produto[i].quantidade}")
    print("+======================================+")
    total = sum([produto.preco * produto.quantidade for produto in lista_carrinho])
    print(f"Total: R${total}")
    print("+======================================+")
    print("1 - Pagar | 2 - Remover P. | 3 - Sair")
    op_carrinho = int(input(""))
    if op_carrinho == 1:
        usuario.saldo -= total
        if usuario.saldo <= 0:
            print("Saldo insuficiente")
        else:
            print("Pagamento realizado com sucesso!")
    elif op_carrinho == 2:
        print("Remover produto do carrinho")
        for i in range(len(lista_carrinho)):
            print(f"{i + 1} - {produto[i].nome}")
        op = int(input("Escolha um produto: "))
        produto_selecionado = produto[op - 1]
        lista_carrinho.remove(produto_selecionado)
    elif op_carrinho == 3:
        print("Sair do carrinho")
        pass
    else:
        print("Opção inválida")
#===============================================

#====================Visual=====================
def pressione_enter():
    input("Pressione enter para Continuar....")
    limpar_tela()

def limpar_tela():
    os.system("cls")
#===============================================

#====================Criar======================
def criar_usuario_novo(lista_usuario):
    _nome = input("Digite o Login: ")
    _idade= input("Digite sua Idade: ")
    _cpf= input("Digite seu CPF: ")
    _telefone=input("Digite seu Telefone: ")
    _senha = getpass.getpass("Digite a senha: ")
    _comfirme_senha = getpass.getpass("Comfirme a Senha: ")
    _saldo = 0
    if _senha == _comfirme_senha:
        print("Usuário Criado com Sucesso!!")
        usuario = Cliente( nome = _nome, senha = _senha, cpf = _cpf, telefone = _telefone, idade = _idade, saldo = _saldo )
        pressione_enter()
        lista_usuario.append(usuario)
    else:
        print("Senha não é igual")
        return False

def adicionar_produto(lista_produtos):

    _nome = input("Digite o Nome do Produto: ")
    _preco = float(input("Digite o Preco do Produto: "))
    _quantidade = input("Digite a Quantidade do Produto: ")
    _produto = Produto(nome = _nome, preco = _preco, quantidade = _quantidade)
    lista_produtos.append(_produto)
    pressione_enter()
    print("Produto Adicionado com Sucesso!!")

def logar_admin():
    _login = input("Digite o Login: ")
    _senha = getpass.getpass("Digite a Senha: ")
    if _login == "admin" and _senha == "admin123":
        print("Login com Sucesso!!")
        return True 
    else:
        print("Login Inválido!!")
        return False       
#===============================================
def painel_usuario(): #Falta completar as funções com dos "IF's" com as "DEF's" do Murilo.
    op = int(input("[OPÇÃO]-> "))
    if op == 1:
        listar_produtos_admin(lista_produtos, lista_carrinho)
    
    elif op == 2:
        #Vizualizar carrinho de compras
        pass


    elif op == 3:
        #Adicionar Saldo
        pass
    
    elif op == 0:
        print("Saindo do Sistema!!")
        exit()

def logar_usuario(): #Falta colocar as novas funções do Murilo.
    usuario=input("Digite seu nome de Usuário: ")
    senha=input("Digite sua Senha: ")
    for _ in range(0,len(lista_usuario)):
        if usuario == lista_usuario[_].nome and senha == lista_usuario[_].senha:
            return True

def painel_adimin():
    op = int(input("[OPÇÃO]-> "))
    if op == 1:
        limpar_tela()
        listar_produtos_admin(lista_produtos)
        limpar_tela()
    
    elif op == 2:
        limpar_tela()
        adicionar_produto(lista_produtos)
        limpar_tela()
    elif op == 3:
        pass

    elif op == 4:
        listar_usuarios_do_sistema(lista_usuario)
    
    elif op == 0:
        print("Saindo do Sistema!!")
        pass