def registro(name="", idade=0, local=""):
 while True:
        try:
                name = str(input("Digite seu nome: ")).strip().split()
                idade = int(input("Digite a sua idade: "))
                local = str(input("Digite o nome de sua cidade: ")).strip().split()
        except (ValueError, AttributeError):
                print("Erro. digite algo válido")
                continue
        break
 return name, idade, local