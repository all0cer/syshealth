def registro(name="", idade=0, local=""):
        name = str(input("Digite seu nome: ")).strip().split()
        idade = int(input("Digite a sua idade: "))
        local = str(input("Digite o nome de sua cidade: ")).strip().split()
        return name, idade, local