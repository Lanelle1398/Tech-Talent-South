# Check the validity of password input by the user. Hint. Re which does matching operations much like Perl.
# Validation:
  # At least 1 letter between [a-z] and 1 letter between [A-Z].
  # At least 1 number between [0-9].
  # At least 1 character from [$#@].
  # Minimum length 6 characters.
  # Maximum length 16 characters.

import re
userInput=input("input your password: ")
y=True
while y: #keep prompting for a new password until the user inputs a valid password
    if not re.search("[a-z]", userInput): 
        print("invalid password missing character a-z")
        break
    elif not re.search("[A-Z]", userInput) :
        print("invalid password missing character A-Z")
        break
    elif not re.search("[0-9]", userInput) : 
        print("invalid password")
        break
    elif not re.search("[$#@]", userInput):
        print("invalid missing character $#@")
        break
    elif(len(userInput)<6 or len(userInput)>16): 
         break
    else:
         print("valid password")
         y=False
         break
