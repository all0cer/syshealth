
def registro(name="", idade=0, sexo=""):
        while True:
                name = input("Digite seu nome: ")
                if all(l.isspace() or l.isalpha() for l in name):
                        break
                else:
                        print(f'Por favor digite um nome válido')
        while True:
                try:
                        idade = int(input("Digite a sua idade: "))
                        break
                except (ValueError, TypeError):
                        print ("Digite apenas números inteiros")
        while True: 
               sexo = input("Digite o sexo(F/M): ").upper()
               if sexo == 'F':
                break
               elif sexo == 'M':
                break        
               else:
                       print(f'Digite F para feminino ou M para masculino')      
        return name, idade, sexo


def historico(historia="",sintomas=""):
        historia = str(input("Digite o histórico de vida do paciente: "))
        sintomas = str(input("Digite os sintomas do paciente: "))
        medicamentos = str(input("Digite o medicamento a ser usado e a dosagem: "))
