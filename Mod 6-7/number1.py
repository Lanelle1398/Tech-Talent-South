# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
index=int(input()) #the user should enter 11 for 11 lines
for i in range(0,index):
    txt = input()
    txt = re.sub(r"(?<= )(&&)(?= )", "and",txt, count=1000)
    # negative and positive look behind.
    # What comes before && must be  a space '&&' what comes after '&&' must also be a space
    # replace the first thousand occurences
    txt = re.sub(r"(?<= )(\|\|)(?= )","or",txt, count=1000)
    print(txt)

