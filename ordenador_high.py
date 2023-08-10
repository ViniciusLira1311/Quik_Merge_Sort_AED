class Sorter:
    def __init__(self):
        pass

    def particiona(self, valores, inicio, fim):
        pivo = valores[inicio]
        i = inicio
        for j in range(inicio + 1, fim + 1):
            if valores[j] <= pivo:
                i += 1
                valores[i], valores[j] = valores[j], valores[i]
        
        valores[inicio], valores[i] = valores[i], valores[inicio]

        return valores, i

    def quick_sort(self, valores, inicio, fim) -> [int]:
        return [1]

    def merge(self, esquerda, direita) -> [int]:
        i = 0
        j = 0
        valores = []
        while(i<len(esquerda) and j<len(direita)):
            if esquerda[i] < direita[j]:
                valores.append(esquerda[i])
                i += 1
            else:
                valores.append(direita[j])
                j += 1
        
        while i < len(esquerda):
            valores.append(esquerda[i])
            i += 1

        
        while j < len(direita):
            valores.append(direita[j])
            j += 1
        
        return valores
    

    def merge_sort(self, valores) -> [int]:
        return [1]
