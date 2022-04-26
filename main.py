import grafo

g3 = grafo.Grafo()
g3.ler_arquivo("grafo3.txt")
print(g3.busca_largura(0))
print(g3.busca_profundidade(0))

desc = [0 for i in range(g3.num_vert)]
R = []
print(g3.busca_profundidade_rec(0, R, desc))

print(g3.conexo(0))
print(g3.ciclo(0))