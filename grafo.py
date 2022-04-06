class Grafo:

  def __init__(self, num_vert = 0, num_arestas = 0, lista_adj = None, mat_adj = None, orientado = False, ponderado = False):
    self.num_vert = num_vert
    self.num_arestas = num_arestas
    self.orientado = orientado
    self.ponderado = ponderado
    if lista_adj is None:
      self.lista_adj = [[] for i in range(num_vert)]
    else:
      self.lista_adj = lista_adj
    if mat_adj is None:
      self.mat_adj = [[0 for j in range(num_vert)] for i in range(num_vert)]
    else:
      self.mat_adj = mat_adj

  def add_aresta(self, u, v, w = 1):
    """Adiciona aresta de u a v com peso w"""
    if u < self.num_vert and v < self.num_vert:
      self.num_arestas += 1
      if not self.orientado and not self.ponderado:
        self.lista_adj[u].append(v)
        self.lista_adj[v].append(u)
        self.mat_adj[u][v] = 1
        self.mat_adj[v][u] = 1
      elif not self.orientado and self.ponderado:
        self.lista_adj[u].append((v, w))
        self.lista_adj[v].append((u, w))
        self.mat_adj[u][v] = w
        self.mat_adj[v][u] = w
      elif self.orientado and not self.ponderado:
        self.lista_adj[u].append(v)
        self.mat_adj[u][v] = 1
      elif self.orientado and self.ponderado:
        self.lista_adj[u].append((v, w))
        self.mat_adj[u][v] = w
    else:
      print("Aresta invalida!")

  def remove_aresta(self, u, v):
    """Remove aresta de u a v, se houver"""
    if u < self.num_vert and v < self.num_vert:
      if self.mat_adj[u][v] != 0:
        self.mat_adj[u][v] = 0
        if not self.ponderado:
          self.lista_adj[u].remove(v)
        else:
          for (v2, w2) in self.lista_adj[u]:
            if v2 == v:
              self.lista_adj[u].remove((v2, w2))
              break
        if not self.orientado:
          self.mat_adj[v][u] = 0
          if not self.ponderado:
            self.lista_adj[v].remove(u)
          else:
            for (u2, w2) in self.lista_adj[v]:
              if u2 == u:
                self.lista_adj[v].remove((u2, w2))
                break
      else:
        print("Aresta inexistente!")
    else:
      print("Aresta invalida!")

  def grau(self, u):
    """Retorna o grau do vertice u"""
    return len(self.lista_adj[u])

  def adjacente(self, u, v):
    """Determina se v é adjacente a u"""
    if self.mat_adj[u][v] != 0:
      return True
    else:
      return False

  def adjacentes(self, u):
    """Retorna a lista dos vertices adjacentes a u"""
    return self.lista_adj[u]

  def ler_arquivo(self, nome_arq):
    """Le arquivo de grafo no formato dimacs"""
    try:
      arq = open(nome_arq)
      #Leitura do cabecalho
      str = arq.readline()
      str = str.split(" ")
      self.num_vert = int(str[0])
      self.num_arestas = int(str[1])
      #Inicializacao das estruturas de dados
      self.lista_adj = [[] for i in range(self.num_vert)]
      self.mat_adj = [[0 for j in range(self.num_vert)] for i in range(self.num_vert)] 
      #Le cada aresta do arquivo
      for i in range(0,self.num_arestas):
        str = arq.readline()
        str = str.split(" ")
        u = int(str[0])
        v = int(str[1])
        w = int(str[2])
        self.add_aresta(u, v, w)
    except IOError:
      print("Nao foi possivel encontrar ou ler o arquivo!")
