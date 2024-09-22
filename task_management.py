# Gestão de tarefas, com as seguintes opções:
# 1) criar nova tarefa 
# 2) listar tarefas (seria printar todas elas) 
# 3) remover uma tarefa 
# 4) limpar tarefas 
# 5) completar uma tarefa 
# 6) mostrar todas tarefas concluidas 
# 7) mostrar tarefas que faltam ser concluidas e as concluidas

tarefas_pendentes = []
tarefas_concluidas = []

def criar_tarefa():
    tarefa = input("Digite uma nova tarefa: ")
    tarefas_pendentes.append(tarefa)
    print(f"Tarefa '{tarefa}' adicionada com sucesso!")

def listar_tarefas():
    print("\nTarefas pendentes:")
    if not tarefas_pendentes:
        print("Nenhuma tarefa pendente.")
    else:
        for idx, tarefa in enumerate(tarefas_pendentes, 1):
            print(f"{idx}. {tarefa}")
    
    print("\nTarefas concluídas:")
    if not tarefas_concluidas:
        print("Nenhuma tarefa concluída.")
    else:
        for idx, tarefa in enumerate(tarefas_concluidas, 1):
            print(f"{idx}. {tarefa}")

def remover_tarefa():
    listar_tarefas()
    try:
        numero = int(input("\nDigite o número da tarefa que deseja remover: "))
        if 1 <= numero <= len(tarefas_pendentes):
            tarefa_removida = tarefas_pendentes.pop(numero - 1)
            print(f"Tarefa '{tarefa_removida}' removida com sucesso!")
        elif 1 <= numero - len(tarefas_pendentes) <= len(tarefas_concluidas):
            tarefa_removida = tarefas_concluidas.pop(numero - len(tarefas_pendentes) - 1)
            print(f"Tarefa '{tarefa_removida}' removida com sucesso!")
        else:
            print("Número inválido.")
    except ValueError:
        print("Por favor, insira um número válido.")

def limpar_tarefas():
    tarefas_pendentes.clear()
    tarefas_concluidas.clear()
    print("Todas as tarefas foram removidas!")

def completar_tarefa():
    listar_tarefas()
    try:
        numero = int(input("\nDigite o número da tarefa que deseja marcar como concluída: "))
        if 1 <= numero <= len(tarefas_pendentes):
            tarefa_concluida = tarefas_pendentes.pop(numero - 1)
            tarefas_concluidas.append(tarefa_concluida)
            print(f"Tarefa '{tarefa_concluida}' marcada como concluída!")
        else:
            print("Número inválido.")
    except ValueError:
        print("Por favor, insira um número válido.")

def mostrar_tarefas_concluidas():
    print("\nTarefas concluídas:")
    if not tarefas_concluidas:
        print("Nenhuma tarefa concluída.")
    else:
        for idx, tarefa in enumerate(tarefas_concluidas, 1):
            print(f"{idx}. {tarefa}")

def mostrar_todas_tarefas():
    print("\nTarefas pendentes:")
    if not tarefas_pendentes:
        print("Nenhuma tarefa pendente.")
    else:
        for idx, tarefa in enumerate(tarefas_pendentes, 1):
            print(f"{idx}. {tarefa}")
    
    mostrar_tarefas_concluidas()

def menu():
    while True:
        print("\nGestão de Tarefas")
        print("1) Criar nova tarefa")
        print("2) Listar tarefas")
        print("3) Remover uma tarefa")
        print("4) Limpar tarefas")
        print("5) Completar uma tarefa")
        print("6) Mostrar tarefas concluídas")
        print("7) Mostrar tarefas pendentes e concluídas")
        print("0) Sair")
        
        option = input("Escolha uma opção: ")
        
        if option == '1':
            criar_tarefa()
        elif option == '2':
            listar_tarefas()
        elif option == '3':
            remover_tarefa()
        elif option == '4':
            limpar_tarefas()
        elif option == '5':
            completar_tarefa()
        elif option == '6':
            mostrar_tarefas_concluidas()
        elif option == '7':
            mostrar_todas_tarefas()
        elif option == '0':
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida, escolha uma opção válida.")

menu()
