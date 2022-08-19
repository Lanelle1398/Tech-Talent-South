

import re
index=int(input()) #loop twice; user should enter 2
for i in range(index):
        txt=input() #get line1, then line 2 etc
        if bool(re.search("<[a-z](\w|-|_|\.)+@[a-z]+\.[a-z]{1,3}>", txt)):
            lst = re.findall('^([\w\-]+)', (txt))  
            lst2=re.findall(r'<[\w.+-]+@[\w-]+\.[\w.-]+>', txt)
            print(*(lst +lst2))
 
        
