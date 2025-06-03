def quick_sort(arr):
    def _quick_sort(lista, low, high):
        if low < high:
            pi = partition(lista, low, high)
            _quick_sort(lista, low, pi - 1)
            _quick_sort(lista, pi + 1, high)

    def partition(lista, low, high):
        # Novo pivô: elemento do meio
        meio = (low + high) // 2
        lista[meio], lista[high] = lista[high], lista[meio]  # Move o pivô para o final
        pivot = lista[high]

        i = low - 1
        for j in range(low, high):
            if lista[j] <= pivot:
                i += 1
                lista[i], lista[j] = lista[j], lista[i]
        lista[i + 1], lista[high] = lista[high], lista[i + 1]
        return i + 1

    _quick_sort(arr, 0, len(arr) - 1)
