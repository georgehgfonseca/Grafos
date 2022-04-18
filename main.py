import grafo

g3 = grafo.Grafo()
g3.ler_arquivo("grafo3.txt")
print(g3.busca_largura(0))
