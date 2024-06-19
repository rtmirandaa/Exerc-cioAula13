from pilha import pilha
from livro import livro

l1 = livro("livro1", "autor1", 100)
l2 = livro("livro2", "autor2", 200)
l3 = livro("livro3", "autor3", 300)

p = pilha()
p.add(l1)
p.add(l2)
p.add(l3)

print("Pilha inicial:")
p.imprimir()

print("\nRemovendo o topo da pilha:")
p.remover()
p.imprimir()