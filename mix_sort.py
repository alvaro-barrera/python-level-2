import random


def mixt_sort(list):
    if len(list) > 1:
        middle = len(list) // 2
        left = list[:middle]
        right = list[middle:]
        print(left, '*' * 5, right)

        # llamada recursiva en cada mitad
        mixt_sort(left)
        mixt_sort(right)

        # Iteradores para recorrer las dos sublists
        i = 0
        j = 0
        # Iterador para la list principal
        k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                list[k] = left[i]
                i += 1
            else:
                list[k] = right[j]
                j += 1

            k += 1

        while i < len(left):
            list[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            list[k] = right[j]
            j += 1
            k += 1

        print(f'left {left}, right {right}')
        print(list)
        print('-' * 50)

    return list


if __name__ == '__main__':
    tamano_de_list = int(input('¿De que tamaño será la lista?: '))

    list = [random.randint(0, 100) for i in range(tamano_de_list)]
    print(list)
    print('-' * 20)

    list_ordenada = mixt_sort(list)
    print(list_ordenada)
