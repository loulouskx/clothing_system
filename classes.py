class Produto: # classe pai que define produtos
    def __init__(self, codigo, nome, preco): # construtor
        self.codigo = codigo
        self.nome = nome
        self.preco = preco
        
class Roupa(Produto): # classe que herda de produtos
    def __init__(self, codigo, nome, preco, tamanho): # construtor + tamanho
        super().__init__(codigo, nome, preco) # chama o construtor da classe pai para iniciar os atributos herdados
        self.tamanho = tamanho 

class Acessorio(Produto):
    def __init__(self, codigo, nome, preco, tipo): # construtor + tipo
        super().__init__(codigo, nome, preco) # chama o construtor da classe pai para iniciar os atributos herdados
        self.tipo = tipo

class Usuario: # classe que define usuários
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha

class Loja: # classe que gerencia produtos e usuários
    def __init__(self): # construtor
        self.produtos = []
        self.usuarios = []
        self.usuario_logado = None # define usuário logado inicialmente 

    def adicionar_produto(self, produto): # adiciona produto à lista de produtos
        self.produtos.append(produto)

    def buscar_produto(self, codigo):
        for produto in self.produtos: # recebe um código como argumento 
            if produto.codigo == codigo:
                return produto # retorna produto na lista de produtos
        return None

    def adicionar_usuario(self, usuario): # adiciona usuário à lista de usuários
        self.usuarios.append(usuario)

    def buscar_usuario(self, email, senha):
        for usuario in self.usuarios: # recebe email e senha como argumentos
            if usuario.email == email and usuario.senha == senha: 
                return usuario # retorna usuário na lista de usuários
        return None
    
    def inserir_produto(self, codigo, nome, preco, tipo_ou_tamanho): # insere novo produto na lista de produtos
        if isinstance(tipo_ou_tamanho, str): # verifica se o quinto parametro inserido é string, se sim define como acessório
            produto = Acessorio(codigo, nome, preco, tipo_ou_tamanho) 
        elif isinstance(tipo_ou_tamanho, int): # verifica se o quinto parametro inserido é int, se sim define como roupa2
            produto = Roupa(codigo, nome, preco, tipo_ou_tamanho) 
        else:
            return None
        
        self.produtos.append(produto)
        return produto

    def cadastrar_usuario(self, nome, email, senha): 
        if self.buscar_usuario(email): # verifica se já existe um usuário com o mesmo email
            return None
        else:
            usuario = Usuario(nome, email, senha)
            self.adicionar_usuario(usuario) # adiciona usuario a lista de usuarios
            return usuario