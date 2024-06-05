import heapq

class Tarefa:
    def __init__(self, titulo, descricao, prioridade, prazo=None, concluida=False):
        self.titulo = titulo
        self.descricao = descricao
        self.prioridade = prioridade
        self.prazo = prazo
        self.concluida = concluida

    def __lt__(self, outra):
        return self.prioridade < outra.prioridade

    def marcar_como_concluida(self):
        self.concluida = True

    def alterar_prioridade(self, nova_prioridade):
        self.prioridade = nova_prioridade

class ListaPrioridade:
    def __init__(self):
        self.tarefas = []

    def adicionar_tarefa(self, tarefa):
        heapq.heappush(self.tarefas, tarefa)

    def remover_tarefa(self):
        return heapq.heappop(self.tarefas)

    def get_tarefas(self):
        return self.tarefas

class GerenciarTarefas:
    def __init__(self):
        self.tarefas_pendentes = []
        self.tarefas_concluidas = []

    def adicionar_tarefa(self, tarefa):
        self.tarefas_pendentes.append(tarefa)

    def marcar_como_concluida(self, tarefa):
        tarefa.marcar_como_concluida()
        self.tarefas_pendentes.remove(tarefa)
        self.tarefas_concluidas.append(tarefa)

    def get_tarefas_pendentes(self):
        return self.tarefas_pendentes

    def get_tarefas_concluidas(self):
        return self.tarefas_concluidas

class ProcurarTarefas:
    def __init__(self, tarefas):
        self.tarefas = tarefas

    def procurar_por_titulo(self, titulo):
        return [tarefa for tarefa in self.tarefas if titulo in tarefa.titulo]

    def filtrar_por_prioridade(self, prioridade):
        return [tarefa for tarefa in self.tarefas if tarefa.prioridade == prioridade]

def adicionar_tarefa_interativa():
    titulo = input("Digite o título da tarefa: ")
    descricao = input("Digite a descrição da tarefa: ")
    prioridade = int(input("Digite a prioridade da tarefa (de 1 a 5): "))
    return Tarefa(titulo, descricao, prioridade)

def main():
    tarefas = []
    lista = ListaPrioridade()
    gerenciar = GerenciarTarefas()
    procurar = ProcurarTarefas(tarefas)

    while True:
        print("\n=== MENU ===")
        print("1. Adicionar tarefa")
        print("2. Ver tarefas pendentes")
        print("3. Ver tarefas concluídas")
        print("4. Procurar tarefas por título")
        print("5. Filtrar tarefas por prioridade")
        print("6. Alterar prioridade de uma tarefa")
        print("7. Marcar tarefa como concluída")
        print("8. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            tarefa = adicionar_tarefa_interativa()
            tarefas.append(tarefa)
            lista.adicionar_tarefa(tarefa)
            gerenciar.adicionar_tarefa(tarefa)
            print("Tarefa adicionada com sucesso!")
        elif opcao == '2':
            print("\n=== Tarefas Pendentes ===")
            # Ordena as tarefas pendentes pela prioridade
            tarefas_pendentes_ordenadas = sorted(gerenciar.get_tarefas_pendentes(), key=lambda x: x.prioridade)
            for tarefa in tarefas_pendentes_ordenadas:
                status = "Concluída" if tarefa.concluida else "Pendente"
                print(f"{tarefa.titulo} - Prioridade: {tarefa.prioridade} - Status: {status}")
        elif opcao == '3':
            print("\n=== Tarefas Concluídas ===")
            for tarefa in gerenciar.get_tarefas_concluidas():
                print(f"{tarefa.titulo} - Prioridade: {tarefa.prioridade}")
        elif opcao == '4':
            titulo = input("Digite o título da tarefa que deseja procurar: ")
            encontradas = procurar.procurar_por_titulo(titulo)
            if encontradas:
                print("\n=== Tarefas Encontradas ===")
                for tarefa in encontradas:
                    print(f"{tarefa.titulo} - Prioridade: {tarefa.prioridade}")
            else:
                print("Nenhuma tarefa encontrada com esse título.")
        elif opcao == '5':
            prioridade = int(input("Digite a prioridade que deseja filtrar (de 1 a 5): "))
            filtradas = procurar.filtrar_por_prioridade(prioridade)
            if filtradas:
                print("\n=== Tarefas Filtradas ===")
                for tarefa in filtradas:
                    print(f"{tarefa.titulo} - Prioridade: {tarefa.prioridade}")
            else:
                print("Nenhuma tarefa encontrada com essa prioridade.")
        elif opcao == '6':
            titulo = input("Digite o título da tarefa que deseja alterar a prioridade: ")
            encontradas = procurar.procurar_por_titulo(titulo)
            if encontradas:
                nova_prioridade = int(input("Digite a nova prioridade (de 1 a 5): "))
                for tarefa in encontradas:
                    tarefa.alterar_prioridade(nova_prioridade)
                print("Prioridade da tarefa alterada com sucesso!")
            else:
                print("Nenhuma tarefa encontrada com esse título.")
        elif opcao == '7':
            titulo = input("Digite o título da tarefa que deseja marcar como concluída: ")
            encontradas = procurar.procurar_por_titulo(titulo)
            if encontradas:
                for tarefa in encontradas:
                    gerenciar.marcar_como_concluida(tarefa)
                print("Tarefa marcada como concluída com sucesso!")
            else:
                print("Nenhuma tarefa encontrada com esse título.")
        elif opcao == '8':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()



