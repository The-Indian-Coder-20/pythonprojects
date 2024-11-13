import random
import pandas as pd
from xlsxwriter import Workbook

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
lenLists.sort()
for i in range(len(finalList)):
    for num in range(lenLists[-1]-len(finalList[i])):
        finalList[i].append(0)

df_finalList = pd.DataFrame(finalList).transpose()

while len(finalList[0]) != 0:
    tempList2 = []
    for j in range(3):
        for i in range(len(finalList)):
            while finalList[i] and len(tempList2) < 3:
                    tempList2.append(finalList[i].pop(0))
                    break
            if len(tempList2) >= 3:
                break
    avgList.append(round(sum(tempList2) / len(tempList2), 2))

timeList = []
for i in range(len(avgList)):
    timeList.append(i)

print(avgList)
print(timeList)
 # Time elapsed is based on the max length of the trials
df_finalList['Nuclei Remaining'] = avgList
df_finalList['Time Elapsed'] = timeList

# Save the results to an Excel file
with pd.ExcelWriter("dicesimulation.xlsx", engine="xlsxwriter") as writer:
    df_finalList.to_excel(writer, index=False, header=[f'Trial {i+1}' for i in range(numberOfLists)] + ['Nuclei Remaining'] + ['Time Elapsed'], sheet_name='Simulation Data')

print(f"Simulation results saved in 'dicesimulation.xlsx'")