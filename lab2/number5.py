# Iterate through a given list and check if a given element already exists in a dictionary as a key’s value. If not, delete it from the list.
# rollNumber = [47, 64, 69, 37, 76, 83, 95, 97]
# sampleDict ={'Zach':47, 'Emma':69, 'Kelly':76, 'Jason':97}

rollNumber = [47, 64, 69, 37, 76, 83, 95, 96, 97]
sampleDict = {"Jhon": 47, "Emma": 69, "Kelly": 76, "Jason": 97}

for currentVal in rollNumber[:]:
    if not currentVal in sampleDict.values():
        rollNumber.remove(currentVal)

print(rollNumber)

