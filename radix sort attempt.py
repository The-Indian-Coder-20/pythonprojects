def radixSort(numList):
    numSortList, finalList, x = [], [], 1
    while x <= len(str(max(numList))):
        numSortList.append([])
        x += 1
    for i in range(len(numList)):
        for j in range(len(str(numList[i]))):
            numSortList[j].append(int(str(numList[i])[j]))
    for y in numSortList:
        y = y.sort()
    for z in range(len(numSortList[0])):
        for a in range(len(numSortList)):
            finalList.append(int(f"{numSortList[a][z]}"))
    print(numSortList)
    print(finalList)
radixSort([124, 515, 891, 238, 901, 231, 234, 512, 123, 723])
