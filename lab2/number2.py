#Get a space-separated list of integers from the user, create a tuple of those integers. Then compute and print the result of hash(tuple).

spaceSeparatedList = input("enter a space separated list \n")
numberList = spaceSeparatedList.split()
createdTuple=tuple(numberList)
print(hash(createdTuple))
