from funcoes import *
from previwer import *



#Main
while True:
    menu_inicial()
    opt_menu=input("[OPÇÃO]-> ")
    # Registrar Usuário
    if opt_menu =="1":
        limpar_tela()
        criar_usuario_novo(lista_usuario)
    elif opt_menu =="2":
        pass   
    elif opt_menu =="3":
        if logar_admin() == True:
            while True:
                menu_admin()
                painel_adimin()
            
        else:
            print("Login Inválido!")
            pass
    elif opt_menu =="0":
        print("Volte Sempre !!!")
        exit()
    else:
        print("Opção Errada!!")
        pressione_enter()

#Fim_Main