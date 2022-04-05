import grafo

g1 = grafo.Grafo(4)
print(g1.mat_adj)
g1.add_aresta(0, 2)
g1.add_aresta(1, 3)
print(g1.mat_adj)
