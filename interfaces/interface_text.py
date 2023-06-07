def desenhar_interface():
    print("*"*40)
    print("\t1 - Insertion sort")
    print("\t2 - Shell sort")
    print("\t3 - Selection sort")
    print("\t4 - Heap sort")
    print("\t0 - Sair")
    print("*"*40)
    selecao = int(input("Selecione a ordenação:  "))

    while selecao < 0 and selecao > 4:
        print("Numero invalido! Tente novamente.")
        selecao = int(input("Selecione a ordenação:  "))

    return selecao
        
def selection_sort_interface():
    print("*"*20)
    print("\t1 - SHELL")
    print("\t2 - Knuth")
    print("\t3 - Ciura")
    print("*"*20)
    gap = int(input("Selecione a lista de gaps:  "))

    while gap < 1 and gap > 3:
        print("Numero invalido! Tente novamente.")
        gap = int(input("Selecione a lista de gaps:  "))

    if gap == 1:
        return "SHELL"
    elif gap == 2:
        return 'KNUTH'
    else:
        return "CIURA"
    

""" 
lista_selection = [32,7,3,15,13,4,21,6,2,9,1,31,45,11,5,8]

selecao = inter.desenhar_interface()
sorts = sort.sorts(lista_selection, len(lista_selection))

if selecao == 1:
    sorts.insertionSort(solo=True)
elif selecao == 2:
    tipo = inter.selection_sort_interface()
    sorts.insertionSort(tipo = tipo)
elif selecao == 3:
    sorts.selection_sort()
elif selecao == 4:
    sorts.heap_sort()
 """

