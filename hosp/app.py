import register


cadastro = [register.registro()]
for item in cadastro:
    print (f"Nome:{item[0]}")
    print (f"Idade:{item[1]}")
    print (f"Sexo:{item[2]}")

cadastro_historico = register.historico()

