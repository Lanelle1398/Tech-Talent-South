from itertools import combinations_with_replacement
word , numberOfPerms = input(" enter word then number of permutations: \n").split()

for i in combinations_with_replacement(sorted(word),int(numberOfPerms)): #given a word, and number of perms, find permutations, create a list, iterate over that list
      print(*i,sep='')
