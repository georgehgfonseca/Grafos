import grafo

g1 = grafo.Grafo(orientado = True, ponderado = False)
g1.ler_arquivo("grafo1.txt")
print(g1.mat_adj)
