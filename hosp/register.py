def registro(name="", idade=0, local=""):
        while name.isalpha() == False:
                name = input("Digite seu nome: ")
                if name.isalpha():
                        break

                else:
                        print("Por favor digite um nome válido.(Não deve conter espaços)")
        while True:
                try:
                        idade = int(input("Digite a sua idade: "))
                        break
                except (ValueError, TypeError):
                        print ("Digite apenas números inteiros")
        while True:
                try:
                        local = input("Digite o nome de sua cidade: ")
                        if local.isalpha():
                                break
                except (ValueError, TypeError):
                        print("Por favor, digite um local válido.(Não deve conter espaços")
        return name, idade, local