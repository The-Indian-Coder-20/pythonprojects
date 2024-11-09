def radixSort(numList):
    numSortList, finalList, x = [], [], 0
    while x <= len(str(max(numList))):
        numSortList.append([])
    numSortList.append(len(str(max(numList)))*"[]")
    print(numSortList)
    for i in range(len(numList)):
        print("yes")

radixSort([124, 515, 891, 238, 901, 231, 234, 512, 123, 723])
