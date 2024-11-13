import random
import pandas as pd

finalList, startingDiceNum, tempList = [], 50, []
numberOfLists = int(input("How many data trials/sets would you like?: "))
for i in range(numberOfLists):
    finalList.append([])

for j in range(len(finalList)):
    currentDiceNum = startingDiceNum
    while currentDiceNum != 0:
        for num in range(0, currentDiceNum):
            tempList.append(random.randint(0, 6))
        finalList[j].append(currentDiceNum - tempList.count(1))
        currentDiceNum -= tempList.count(1)
        tempList.clear()
avgList, lenLists = [], []
for list in finalList:
    lenLists.append(len(list))
for i in range(len(finalList)):
    if len(finalList[i]) != lenLists[0]:
        print(finalList[i])
        for num in range(lenLists[0]-len(finalList[i])):
            finalList[i].append(0)
# Excel File Writing with pandas
#df = pd.DataFrame(finalList).transpose()  # Make rows columns (transpose allows Excel vertical compatibility)
#df.to_excel("dicesimulation.xlsx", index=False, header=[f'Trial {i+1}' for i in range(numberOfLists)], engine='xlsxwriter')

print(f"Simulation results saved in 'dicesimulation.xlsx'")
