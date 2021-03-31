def insertion_sort(list):
    for index in range(1, len(list)): # O(n)
        value_current = list[index]
        position_current = index

        while position_current > 0 and list[position_current - 1] > value_current: # O(log n)
            list[position_current] = list[position_current - 1]
            position_current -= 1

        list[position_current] = value_current

# COMPELJIDAD O(n log n) : CUASI LINEAL