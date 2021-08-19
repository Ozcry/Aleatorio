def pesquisa_binaria(lista, item):
    baixo = 1
    alto = len(lista) - 1
    while baixo <= alto:
        meio = (baixo + alto) // 2
        chute = lista[meio]
        if chute == item:
            return meio
        elif chute > item:
            alto = meio - 1
        else:
            baixo = meio + 1
    return None


minha_lista = [1, 3, 4, 6, 8, 12, 34, 56]  # Funciona com listas e tuplas
print(pesquisa_binaria(minha_lista, 3))
