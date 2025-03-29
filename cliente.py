# Criando uma lista para armazenar os dados
banco_de_dados = []

# Função para adicionar um cliente
def adicionar_cliente():
    nome = input("Digite o nome do cliente: ")
    idade = int(input("Digite a idade do cliente: "))
    email = input("Digite o email do cliente: ")
    telefone = int(input('Digite o numero do cliente'))
    
    cliente = {
        "nome": nome,
        "idade": idade,
        "email": email,
        'telefone': telefone,
    }
    
    banco_de_dados.append(cliente)
    print(f"Cliente {nome} adicionado com sucesso!")

# Função para listar todos os clientes
def listar_clientes():
    if banco_de_dados:
        print("Lista de Clientes:")
        for cliente in banco_de_dados:
            print(f"Nome: {cliente['nome']}, Idade: {cliente['idade']}, Email: {cliente['email']}", telefone: {cliente['telefone']})
    else:
        print("Nenhum cliente registrado.")

# Função para buscar um cliente pelo nome
def buscar_cliente():
    nome = input("Digite o nome do cliente a ser buscado: ")
    for cliente in banco_de_dados:
        if cliente["nome"].lower() == nome.lower():
            print(f"Cliente encontrado: {cliente['nome']}, Idade: {cliente['idade']}, Email: {cliente['email']}, telefone: {cliente['telefone']}")
            return
    print(f"Cliente {nome} não encontrado.")

# Função para remover um cliente pelo nome
def remover_cliente():
    nome = input("Digite o nome do cliente a ser removido: ")
    global banco_de_dados
    banco_de_dados = [cliente for cliente in banco_de_dados if cliente["nome"].lower() != nome.lower()]
    print(f"Cliente {nome} removido com sucesso.")

# Menu para interagir com o banco de dados
def menu():
    while True:
        print("\n----- MENU -----")
        print("1. Adicionar Cliente")
        print("2. Listar Clientes")
        print("3. Buscar Cliente")
        print("4. Remover Cliente")
        print("5. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            adicionar_cliente()
        elif opcao == "2":
            listar_clientes()
        elif opcao == "3":
            buscar_cliente()
        elif opcao == "4":
            remover_cliente()
        elif opcao == "5":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida! Tente novamente.")

# Executando o menu
menu()
