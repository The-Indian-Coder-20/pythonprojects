def radixSort(numList):
    numSortList, finalList, x = [], [], 1
    while x <= len(str(max(numList))):
        numSortList.append([])
        x += 1
    print(numSortList)
    for i in range(len(numList)):
        print("yes")

radixSort([124, 515, 891, 238, 901, 231, 234, 512, 123, 723])
