import grafo

g1 = grafo.Grafo()
g1.ler_arquivo("grafo1.txt")
print(g1.mat_adj)
g2 = grafo.Grafo()
g2.ler_arquivo("grafo2.txt")
print(g2.mat_adj)
print(g2.subgrafo(g1))
