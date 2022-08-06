
rollNumber = [47, 64, 69, 37, 76, 83, 95, 96, 97]
sampleDict = {"Jhon": 47, "Emma": 69, "Kelly": 76, "Jason": 97}

for currentVal in rollNumber[:]:
    if not currentVal in sampleDict.values():
        rollNumber.remove(currentVal)

print(rollNumber)

