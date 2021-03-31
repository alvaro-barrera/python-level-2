

def bag(bag_size, weight, values, n):

    if n == 0 or bag_size == 0:
        return 0

    if weight[n - 1] > bag_size:
        return bag(bag_size, weight, values, n - 1)

    return max(values[n - 1] + bag(bag_size - weight[n - 1], weight, values, n - 1),
                bag(bag_size, weight, values, n - 1))


if __name__ == '__main__':
    values = [60, 100, 120]
    weight = [10, 20, 30]
    bag_size = 50
    n = len(values)

    response = bag(bag_size, weight, values, n)
    print(response)