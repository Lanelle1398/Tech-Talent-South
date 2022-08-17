import re
index=int(input()) #the user should enter 11 for 11 lines
for i in range(0,index):
   txt = input()
   txt = re.sub(r"\ \&\&\ "," and ",txt)
   txt = re.sub(r"\ \|\|\ "," or ",txt)
#    txt = re.sub(r"\ \&\&\ "," and ",txt)
#    txt = re.sub(r"\ \|\|\ "," or ",txt)
   print(txt)
