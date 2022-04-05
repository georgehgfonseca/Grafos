class Grafo:

  def __init__(self, num_vert, lista_adj = None, mat_adj = None):
    self.num_vert = num_vert
    if lista_adj is None:
      self.lista_adj = [[] for i in range(num_vert)]
    else:
      self.lista_adj = lista_adj
    if mat_adj is None:
      self.mat_adj = [[0 for j in range(num_vert)] for i in range(num_vert)]
    else:
      self.mat_adj = mat_adj

  def add_aresta(self, u, v):
    self.lista_adj[u].append(v)
    self.lista_adj[v].append(u)
    self.mat_adj[u][v] = 1
    self.mat_adj[v][u] = 1

  def grau(self, v):
    return len(self.lista_adj[v])

  def adjacente(self, u, v):
    if self.mat_adj[u][v] != 0:
      return True
    else:
      return False
