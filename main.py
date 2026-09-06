from dados.usuarios import usuarios 

rodando = True

chamados = []

login_digitado = input("login: ")
senha_digitada = input("senha: ")

usuario_logado = None

for usuario in usuarios:
    if usuario["login"] == login_digitado and usuario["senha"] == senha_digitada:
        usuario_logado = usuario

if usuario_logado is None:
    print("Login ou senha incorretos.")
else:
    print("Login realizado com sucesso! Tipo:", usuario_logado["tipo"])

    while rodando:
        print("\n==========================")
        print("  SISTEMA DE CHAMADOS TI  ")
        print("==========================")

        print("1- Abrir chamado")
        print("2- Listar chamados")
        print("3- Consultar chamado")
        print("4- Alterar status")
        print("5- Sair")

        opcao = input("Escolha uma opção: ")

        print("Voce escolheu: ", opcao)

        if opcao == "1":
            print("Voce escolheu abrir um chamado.")
            print("\n--- ABRIR CHAMADO ---")

            nome = input("Nome do solicitante: ")
            titulo = input("Titulo do problema: ")
            descricao = input("Descreva o problema: ")

            print("\nGrau de urgência:")
            print("1 - Baixa")
            print("2 - Media")
            print("3 - Alta")
            print("4 - Critica")

            urgencia = input("Escolha a urgência: ")

            if urgencia == "1":
                urgencia = "Baixa"
            elif urgencia == "2":
                urgencia = "Media"
            elif urgencia == "3":
                urgencia = "Alta"
            elif urgencia == "4":
                urgencia = "Critica"
            else:
                urgencia = "Nao definida"

            novo_id = len(chamados) + 1
            
            chamado = {
                "id": novo_id,
                "nome": nome,
                "titulo": titulo,
                "urgencia": urgencia,
                "status": "Aberto"
            }
            chamados.append(chamado)

            print("Chamado cadastrado com sucesso!")

            print("\n=== Chamado aberto ===")
            print("Nome do solicitante: ", nome)
            print("Titulo: ", titulo)
            print("Descricao: ", descricao)
            print("Urgencia: ", urgencia)
            print("Status: Aberto ")

        elif opcao == "2":
            if len(chamados) == 0:
                print("Nenhum chamado cadastrado ainda.")
            else:
                print("\n=== LISTA DE CHAMADOS ===")
                for chamado in chamados:
                    print("ID:", chamado["id"])
                    print("Nome:", chamado["nome"])
                    print("Titulo:", chamado["titulo"])
                    print("Urgencia:", chamado["urgencia"])
                    print("Status:", chamado["status"])
                    print("-------------------------")
        elif opcao == "3":
            id_busca = input("Digite o ID do chamado que deseja consultar: ")
            id_busca = int(id_busca)

            encontrado = False

            for chamado in chamados:
                if chamado["id"] == id_busca:
                    print("\n=== CHAMADO ENCONTRADO ===")
                    print("ID:", chamado["id"])
                    print("Nome:", chamado["nome"])
                    print("Titulo:", chamado["titulo"])
                    print("Urgencia:", chamado["urgencia"])
                    print("Status:", chamado["status"])
                    encontrado = True
                    break

            if not encontrado:
                print("Chamado não encontrado com esse ID.")

        elif opcao == "4":
            id_busca = input("Digite o ID do chamado que deseja alterar status: ")
            id_busca = int(id_busca)

            encontrado = False

            for chamado in chamados:
                if chamado["id"] == id_busca:
                    encontrado = True

                    print("\nStatus atual,: ", chamado["status"])

                    print("\nNovo status:")
                    print("1 - Aberto")
                    print("2 - Em andamento")
                    print("3 - Resolvido")
                    print("4 - Fechado")

                    novo_status = input("Escolha o novo status:")

                    status_valido = True

                    if novo_status == "1":
                        chamado["status"] = "Aberto"
                    elif novo_status == "2":
                        chamado["status"] = "Em Andamento"
                    elif novo_status == "3":
                        chamado["status"] = "Resolvido"
                    elif novo_status == "4":
                        chamado["status"] = "Fechado"
                    else:
                        status_valido = False
                        print("Opcao invalida, status nao alterado.")

                    if status_valido:
                        print("\nStatus atualizado com sucesso!")
                        print("Novo status:", chamado["status"])
            if not encontrado:
                print("Nenhum chamado encontrado com esse ID.")

        elif opcao == "5":
            print("Saindo do sistema...")
            rodando = False

        else:
            print("Opcao invalida.")