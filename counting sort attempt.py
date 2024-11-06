countingList = [2, 3, 0, 2, 3, 2]
midList = []
finalList = []
i = 0
while i <= max(countingList):
    midList.append(0)
    i += 1
for i in countingList:
    midList[i] += 1
print(midList)
for i in range(len(midList)):
    j = 1
    while j <= midList[i]:
        finalList.append(i)
        j += 1
print(finalList)