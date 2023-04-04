from classes import *

loja = Loja() # instância de loja


def main():
    while True:
        if loja.usuario_logado: # verifica se está logado
            opcao = input("Selecione uma opção:\n1 - Inserir produto\n2 - Consultar produto\n3 - Logout\n")
            
            if opcao == "1": # pede os atributos de produto
                codigo = input("Digite o código do produto: ")
                nome = input("Digite o nome do produto: ")
                preco = float(input("Digite o preço do produto: "))
                classe = input("O produto é acessório ou roupa? ") # pede a classe para saber quarto parametro
                
                if classe == "Acessorio": # se for acessorio adiciona na lista com tipo
                    tipo = input("Digite o tipo do acessório: ")
                    loja.inserir_produto(codigo, nome, preco, tipo)
                    print("Produto adicionado.")
                elif classe == "Roupa":
                    tamanho = input("Digite o tamanho da roupa: ") # se for roupa adiciona na lista com tamanho
                    loja.inserir_produto(codigo, nome, preco, tamanho)
                    print("Produto adicionado.")
                else:
                    print("Categoria inválida.")
                
            elif opcao == "2":
                codigo = input("Digite o código do produto: ")
                produto = loja.buscar_produto(codigo) # verifica se o produto está na lista de produtos
                if produto:
                    print(f"Código: {produto.codigo}\nNome: {produto.nome}\nPreço: R${produto.preco}") # print atributos da classe pai
                    if isinstance(produto, Roupa): # verifica se o produto é uma roupa
                        print(f"Tamanho: {produto.tamanho}")
                    elif isinstance(produto, Acessorio): # verifica se o produto é um acessório
                        print(f"Tipo: {produto.tipo}")
                else:
                    print("Produto não encontrado.")


                    
            elif opcao == "3": # retorna o estado do usuario logado ao inicial aka desloga
                loja.usuario_logado = None
                print("Usuário deslogado.")
                
            else:
                print("Opção inválida.")
                
        else: # caso usuario_logado = None (estado inicial)
            opcao = input("Selecione uma opção:\n1 - Login\n2 - Cadastrar usuário\n3 - Sair\n")
            
            if opcao == "1": # pede atributos de usuario
                email = input("Digite o e-mail do usuário: ")
                senha = input("Digite a senha do usuário: ")
                usuario = loja.buscar_usuario(email, senha) # busca atributos na lista de usuarios
                if usuario:
                    loja.usuario_logado = usuario # armazena a instância usuario_logado em usuario
                    print(f"Bem-vindo(a), {usuario.nome}!")
                else:
                    print("Usuário inválido.")   
                    
            elif opcao == "2": # coleta atributos de usuario
                nome = input("Usuário: ")
                email = input("Digite o e-mail do usuário: ")
                senha = input("Digite a senha do usuário: ")
                usuario = Usuario(nome, email, senha) # cria usuário com tais atributos
                loja.adicionar_usuario(usuario) # adiciona à lista de usuários
                print("Usuário cadastrado com sucesso.")
                
            elif opcao == "3": # encerra o programa
                print("Saindo.")
                break
            else:
                print("Opção inválida.")


if __init__ == '__name__':
    main()