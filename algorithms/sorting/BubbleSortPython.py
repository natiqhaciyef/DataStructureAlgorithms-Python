def bubbleSort(arrList):
    n = len(arrList)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arrList[j] > arrList[j + 1]:
                arrList[j], arrList[j + 1] = arrList[j + 1], arrList[j]


