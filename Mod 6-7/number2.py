
import re
index=int(input()) #loop twice; user should enter 2
for i in range(index):
        txt=input() #get line1, then line 2 etc
        if bool(re.search("<[a-z](\w|-|_|\.)+@[a-z]+\.[a-z]{1,3}>", txt)): #if you find this pattern in the text, print out the entire string
            print(txt)
       
# import email.utils
# import email.utils
# import re
# n = int(input())
# for i in range(n):
#     p = email.utils.parseaddr(input())
#     if re.match(r'[a-z][\w.-]+@[a-z]+\.[a-z]{1,3}$', p[1], re.I):
#         #print (formataddr(p))
#         print(email.utils.formataddr(p))
//other methodd

# import re
# index=int(input()) #loop twice; user should enter 2
# for i in range(index):
#         txt=input() #get line1, then line 2 etc
#         if bool(re.search("<[a-z](\w|-|_|\.)+@[a-z]+\.[a-z]{1,3}>", txt)):
#             lst = re.findall('^([\w\-]+)', (txt))  
#             lst2=re.findall(r'<[\w.+-]+@[\w-]+\.[\w.-]+>', txt)
#             print(*(lst +lst2))
#         # +
        
#         # Printing of List 
#         #print(lst)
        
