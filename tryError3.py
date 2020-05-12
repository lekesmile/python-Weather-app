# import sys

# while True:
#     try:

  
#        askedNum = float(input("Give a number: "))
#        print("Given number rounded:", round(askedNum, 2))
#     except:
#        if askedNum.is_integer != False:
#          print("Bad input!")
#        else:
#            sys.exit()

import sys
askedNum= ''
while True:

       try:
          askedNum = input("Give a number: ")
          if askedNum == "quit":
             sys.exit()
          print("Given number rounded:", round(float(askedNum), 2))
       except ValueError:
         print("Bad input!")

       
    