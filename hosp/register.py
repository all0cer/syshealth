
def registro(
        name="", idade=0, sexo=""
        ):
        """Está função exerce o cadastro de um novo paciente com as seguinte informações:
           \nName: Nome do paciente
           \nIdade: Idade do paciente
           \nSexo: Sexo do paciente(F/M)"""
        while True:
                name = input(
                        "Digite seu nome: "
                        )
                if all(
                        l.isspace() or l.isalpha() for l in name
                        ):
                        break
                else:
                        print(
                                f'Por favor digite um nome válido'
                                )
        while True:
                try:
                        idade = int(
                                input(
                                        "Digite a sua idade: "
                                        )
                                )
                        break
                except (
                        ValueError, TypeError
                        ):
                        print (
                                "Digite apenas números inteiros"
                                )
        while True: 
               sexo = input(
                       "Digite o sexo(F/M): "
                       ).upper()

               if sexo == 'F':

                break

               elif sexo == 'M':

                break        

               else:

                       print(
                               f'Digite F para feminino ou M para masculino'
                               )   

        return name, idade, sexo


def historico(
        historia="",sintomas="",medicamentos=""
        ):
        """Histótia: Adicionar os relatos de doenças anteriores do paciente,\n incluindo sintomas antigos e histórico de doenças familiares
        \n Sintomas: Descrever os atuais sintomas do paciente 
        \n Medicamentos: Remédios e tratamentos usados durante o tratamento geral do paciente."""
        historia = str(
                input(
                        "Digite o histórico de vida do paciente: "
                        )
                )
        sintomas = str(
                input(
                        "Digite os sintomas do paciente: "
                        )
                )
        medicamentos = str(
                input(
                        "Digite o medicamento a ser usado e a dosagem: "
                        )
                )

