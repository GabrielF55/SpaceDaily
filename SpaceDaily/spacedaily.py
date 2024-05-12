#Importando biblioteca para uso de lista prioritária.
import heapq

#Criando a classe Tarefa, envolvendo os atributos titulo, descricao, prioridade e prazo.
class Tarefa:
    def _init_(self, titulo, descricao, prioridade, prazo=None):
        self.titulo = titulo
        self.descricao = descricao
        self.prioridade = prioridade
        self.prazo = prazo

    def _lt_(self, outra):
        return self.prioridade < outra.prioridade

#Classe envolvendo a prioridade da lista.
class ListaPrioridade:
    def _init_(self):
        self.tarefas = []

    def adicionar_tarefa(self, tarefa):
        heapq.heappush(self.tarefas, tarefa)

    def remover_tarefa(self):
        return heapq.heappop(self.tarefas)

    def get_tarefas(self):
        return self.tarefas

#Classe envolvendo a parte de gerenciamento.
class GerenciarTarefas:
    def _init_(self):
        self.tarefas_pendentes = []
        self.tarefas_concluidas = []

    def adicionar_tarefa(self, tarefa):
        self.tarefas_pendentes.append(tarefa)

    def marcar_como_completo(self, tarefa):
        self.tarefas_pendentes.remove(tarefa)
        self.tarefas_concluidas.append(tarefa)

    def get_tarefas_pendentes(self):
        return self.tarefas_pendentes

    def get_tarefas_concluidas(self):
        return self.tarefas_concluidas

#Essa classe serve para procurar, dentre as tarefas, a pesquisa desejada.
class ProcurarTarefas:
    def _init_(self, tarefas):
        self.tarefas = tarefas

    def procurar_por_titulo(self, titulo):
        return [tarefa for tarefa in self.tarefas if titulo in tarefa.titulo]

    def procurar_por_descricao(self, descricao):
        return [tarefa for tarefa in self.tarefas if descricao in tarefa.descricao]

    def filtrar_por_prioridade(self, prioridade):
        return [tarefa for tarefa in self.tarefas if tarefa.prioridade == prioridade]

    def filtrar_por_prazo(self, prazo):
        
        return [tarefa for tarefa in self.tarefas if tarefa.prazo <= prazo]

#Aqui separei todos os testes necessários.
#Utilizei do f-string por motivo de preferência e estética.
tarefas = [Tarefa("Acordar", "Acordar de 07h30", 2), Tarefa("Comer", "Tomar café da manhã", 4), 
           Tarefa("Programar", "Continuar o desenvolvimento de Estrutura de Dados", 1)]
lista =   ListaPrioridade()
gerenciar = GerenciarTarefas()
procurar = ProcurarTarefas(tarefas)

for tarefa in tarefas:
    lista.adicionar_tarefa(tarefa)

print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
print("Tarefas em ordem de prioridade:")
print()
for tarefa in lista.get_tarefas():
    print(f"{tarefa.titulo} - Prioridade: {tarefa.prioridade}")

gerenciar.adicionar_tarefa(tarefas[0])
gerenciar.adicionar_tarefa(tarefas[1])

print()
print("=-=-=-=-=-=-=-=-=-")
print("Tarefas pendentes:")
print()
for tarefa in gerenciar.get_tarefas_pendentes():
    print(f"{tarefa.titulo} - Prioridade: {tarefa.prioridade}")

gerenciar.marcar_como_completo(tarefas[0])

print()
print("=-=-=-=-=-=-=-=-=-=")
print("Tarefas concluídas:")
print()
for tarefa in gerenciar.get_tarefas_concluidas():
    print(f"{tarefa.titulo} - Prioridade: {tarefa.prioridade}")

print()
print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
print("Tarefas com 'Acordar' no título:")
print()
for tarefa in procurar.procurar_por_titulo("Acordar"):
    print(f"{tarefa.titulo} - Prioridade: {tarefa.prioridade}")

print()
print("=-=-=-=-=-=-=-=-=-=-=-=-=")
print("Tarefas com prioridade 4:")
print()
for tarefa in procurar.filtrar_por_prioridade(4):
    print(f"{tarefa.titulo} - Prioridade: {tarefa.prioridade}")
