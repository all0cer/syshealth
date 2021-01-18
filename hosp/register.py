def registro(name="", idade=0, local=""):
        while name.isalpha() == False:
                name = input("Digite seu nome: ")
                if name.isalpha():
                        name.isalpha() == True
                else:
                        print("Por favor digite um nome válido.(Não deve conter espaços)")
        while True:
                try:
                        idade = int(input("Digite a sua idade: "))
                        break
                except (ValueError, TypeError):
                        print ("Digite apenas números inteiros")
                        
        local = str(input("Digite o nome de sua cidade: ")).strip().split()
        return name, idade, local