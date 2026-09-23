def dynamicArray(n, queries):
    arr = [[] for _ in range(n)]
    lastAnswer = 0
    result = []

    for query in queries:
        q = query[0]
        x = query[1]
        y = query[2]

        index = (x ^ lastAnswer) % n

        if q == 1:
            arr[index].append(y)

        elif q == 2:
            lastAnswer = arr[index][y % len(arr[index])]
            result.append(lastAnswer)

    return result
