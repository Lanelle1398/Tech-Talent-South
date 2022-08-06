# Exercise 4
# Take the following list. Slice it into three equal chunks and reverse each list.
newList=[]
sliceBy=3
sampleList = [11, 45, 8, 23, 14, 12, 78, 45, 89]
for i in range(0, len(sampleList), sliceBy): # i iterates by 3
    #sampleList[i:i+sliceBy]
    newList.append(sampleList[i:i+sliceBy]) # add the sliced values to a new list
    #get from 0 to 3: 11,45, 8
    #go from 3 to 6:23,14,12
    #lNumbergo  from 6 to 9: 78,45,89

#reverse the list
newList.reverse()
print(newList)


