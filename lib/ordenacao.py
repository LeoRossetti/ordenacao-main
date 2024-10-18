
def bubble_sort(lista: list) -> None:
    for i in lista:
        j = i + 1
        if i > j:
            j = i
            lista[j] = lista[i]
            print(lista)
