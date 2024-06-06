import unittest
from spacedaily import Tarefa, ListaPrioridade, GerenciarTarefas, ProcurarTarefas

class TestTarefa(unittest.TestCase):
    def setUp(self):
        self.tarefa = Tarefa("Tarefa 1", "Descrição 1", 3)

    def test_marcar_como_concluida(self):
        self.assertFalse(self.tarefa.concluida)
        self.tarefa.marcar_como_concluida()
        self.assertTrue(self.tarefa.concluida)

    def test_alterar_prioridade(self):
        self.assertEqual(self.tarefa.prioridade, 3)
        self.tarefa.alterar_prioridade(5)
        self.assertEqual(self.tarefa.prioridade, 5)

class TestListaPrioridade(unittest.TestCase):
    def setUp(self):
        self.lista = ListaPrioridade()
        self.tarefa1 = Tarefa("Tarefa 1", "Descrição 1", 1)
        self.tarefa2 = Tarefa("Tarefa 2", "Descrição 2", 2)
        self.lista.adicionar_tarefa(self.tarefa1)
        self.lista.adicionar_tarefa(self.tarefa2)

    def test_adicionar_tarefa(self):
        self.assertEqual(len(self.lista.get_tarefas()), 2)

    def test_remover_tarefa(self):
        tarefa = self.lista.remover_tarefa()
        self.assertEqual(tarefa.titulo, "Tarefa 1")
        self.assertEqual(len(self.lista.get_tarefas()), 1)

class TestGerenciarTarefas(unittest.TestCase):
    def setUp(self):
        self.gerenciar = GerenciarTarefas()
        self.tarefa = Tarefa("Tarefa 1", "Descrição 1", 1)
        self.gerenciar.adicionar_tarefa(self.tarefa)

    def test_adicionar_tarefa(self):
        self.assertEqual(len(self.gerenciar.get_tarefas_pendentes()), 1)

    def test_marcar_como_concluida(self):
        self.gerenciar.marcar_como_concluida(self.tarefa)
        self.assertEqual(len(self.gerenciar.get_tarefas_pendentes()), 0)
        self.assertEqual(len(self.gerenciar.get_tarefas_concluidas()), 1)
        self.assertTrue(self.tarefa.concluida)

class TestProcurarTarefas(unittest.TestCase):
    def setUp(self):
        self.tarefa1 = Tarefa("Tarefa 1", "Descrição 1", 1)
        self.tarefa2 = Tarefa("Tarefa 2", "Descrição 2", 2)
        self.procurar = ProcurarTarefas([self.tarefa1, self.tarefa2])

    def test_procurar_por_titulo(self):
        encontradas = self.procurar.procurar_por_titulo("Tarefa 1")
        self.assertEqual(len(encontradas), 1)
        self.assertEqual(encontradas[0].titulo, "Tarefa 1")

    def test_filtrar_por_prioridade(self):
        filtradas = self.procurar.filtrar_por_prioridade(1)
        self.assertEqual(len(filtradas), 1)
        self.assertEqual(filtradas[0].prioridade, 1)

if __name__ == "__main__":
    unittest.main()
