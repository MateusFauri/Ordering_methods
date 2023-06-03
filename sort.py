import time
import subprocess

class sorts(object):
    def __init__(self, lista, tamanho):
        self.lista = lista
        self.tamanho = tamanho

    def heap_sort(self):
        _heap = self.tamanho
        print(self.lista)
        
        self._build_heap() 
        print(self.lista)

        for nodo_max in range (_heap - 1, 0, -1):
            _auxiliar = self.lista[0]
            self.lista[0] = self.lista[nodo_max]
            self.lista[nodo_max] = _auxiliar
            _heap -= 1
            self._max_heapify(0, _heap)
            print(self.lista)

    def selection_sort(self):
        print(self.lista)
        for index in range(self.tamanho):
            _min = index
            for next in range(index, self.tamanho):
                if self.lista[next] < self.lista[_min]:
                    _min = next
            if _min != index:
                aux = self.lista[index]
                self.lista[index] = self.lista[_min]
                self.lista[_min] = aux
            print(self.lista)

    def shell_sort(self, tipo = 'SHELL'):
        lista_gap = []

        if tipo == 'SHELL':
            lista_potencia_2 = []
            self._potencia_2(lista_potencia_2)
            lista_gap = lista_potencia_2.copy()
        elif tipo == 'KNUTH':
            lista_knuth = []
            self._knuth(lista_knuth)
            lista_gap = lista_knuth.copy()
        elif tipo == 'CIURA':
            lista_ciura = []
            self._ciura(lista_ciura)
            lista_gap = lista_ciura.copy()
        else:
            print("Escrever mensagem de erro!")
            pass
        
        lista_gap.reverse()
        print(self.lista)

        for gap in lista_gap:
            for inicio in range(gap): 
                self.insertionSort(inicio, gap)

            print(self.lista)

    def insertionSort(self, inicio = 0, gap = 1, solo=False):
        if solo:
            print(self.lista)

        for elemento in range(inicio + gap, self.tamanho, gap):
            chave = int(self.lista[elemento])
            number = int(elemento)
            while number >= gap and int(self.lista[number-gap]) > chave:
                self.lista[number] = self.lista[number - gap]
                number -= gap
            self.lista[number] = chave

            if solo:
                print(self.lista)

    def _potencia_2(self, gaps):
        number = i = 1
        while number < self.tamanho:
            gaps.append(number)
            number = 2 ** i
            i += 1

    def _knuth(self, gaps):
        h=1
        gaps.append(h)
        while h < self.tamanho / 3:
            h = 3*h + 1
            gaps.append(h)

    def _ciura(self, gaps):
        ciura = [1,4,10,23,57,132,301,701,1577,3548,7983,17961,40412,90927,204585,460316,1035711]
        for element in ciura:
            if element < self.tamanho:
                gaps.append(element)
            else:
                break
                
    def _build_heap(self):
        for nodo in range (int(self.tamanho/2), -1, -1):
            self._max_heapify(nodo, self.tamanho)

    def _max_heapify(self, posicao, tamanho):
        _left = (2 * posicao) + 1   
        _right = (2 * posicao) + 2
        
        if _left < tamanho and self.lista[_left] > self.lista[posicao]:
            _max = _left
        else:
            _max = posicao

        if _right < tamanho and self.lista[_right] > self.lista[_max]:
            _max = _right

        if _max != posicao:
            _auxiliar = self.lista[posicao]
            self.lista[posicao] = self.lista[_max]
            self.lista[_max] = _auxiliar
            self._max_heapify(_max, tamanho)

