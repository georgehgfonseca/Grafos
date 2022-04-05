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

  def add_aresta(self, s, t):
    self.lista_adj[s].append(t)
    self.lista_adj[t].append(s)
    self.mat_adj[s][t] = 1
    self.mat_adj[t][s] = 1
