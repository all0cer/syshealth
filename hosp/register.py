def registro(name, idade, local):
    while True:
        name = input("Digite seu nome: ").strip().split
        try:
            idade = input(int("Digite a sua idade: "))
        except:
            "Por favor, digite uma idade válida"
        local = input("Digite o nome de sua cidade").split().strip
        if name or idade or local == "":
            "Digite algo"
        else:
            break

        return name, idade, local
        