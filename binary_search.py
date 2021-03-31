import random

def binary_search(list, start, end, target):
    print(f'buscando {target} entre {list[start]} y {list[end - 1]}')
    if start > end:
        return False

    middle = (start + end) // 2

    if list[middle] == target:
        return True
    elif list[middle] < target:
        return binary_search(list, middle + 1, end, target)
    else:
        return binary_search(list, start, middle - 1, target)


if __name__ == '__main__':
    list_size = int(input('¿De qué tamaño es la lista?: '))
    target = int(input('¿Qué número quieres encontrar?: '))

    list = sorted([random.randint(0, 100) for i in range(list_size)])

    found = binary_search(list, 0, len(list), target)

    print(list)
    print(f'El elemento {target} {"está" if found else "no está"} en la lista')