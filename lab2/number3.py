# Take the following two lists. Create a third list by picking a odd-index elements from the first list and even-index elements from the second.
# listOne = [3, 6, 9, 12, 15, 18, 21]
# listTwo = [4, 8, 12, 16, 20, 24, 28]*

listOne = [3, 6, 9, 12, 15, 18, 21]
listTwo= [4, 8, 12, 16, 20, 24, 28]

y=listOne[1:len(listOne):2] # start at index 1 , iterate till the end of the list, step by 2 
z=listTwo[0:len(listOne):2]
#4,12,20,28
listThree=list(y+z)
print(listThree)
