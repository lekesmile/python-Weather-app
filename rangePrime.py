

totalNumber = 0
primeNumber = 0

lowerRange = int(input("Give the lower bound of the number range: "))
upperRange = int(input("Give the upper bound of the number range: "))

for number in range(lowerRange, upperRange + 1):
      totalNumber += 1
      if number  > 1:
          
        for i in range(2, number):  
            if (number % i) == 0:  
                  print(number, "is not a prime, because",i,"*",number//i , "=" , number)
                  break  
        else:    
                primeNumber += 1     
                print(number, "is a prime.")
                        
      else:        
        print(number, "cannot be prime.")
if totalNumber == 2:
   print("Could not find primes from the test range.")
else:
   print("Searched", totalNumber , "numbers, from which", primeNumber, "were primes.") 
   print("The last found prime was",(totalNumber-2),".")       



        


# lowerRange = int(input("Give the lower bound of the number range: "))
# upperRange = int(input("Give the upper bound of the number range: "))

# for number in range(lowerRange, upperRange + 1):
#     if number > 1:
#         for i in range(2,number):  
#            if (number % i) == 0:  
#                print(number, "is not a prime, because " + str(2) + " * " +
#                   str(round(number/2)) + " =" , i * round(number/2))
#                break  
#         else:         
#             print(number, "is a prime.")
#     else:
#         print(number, "cannot be prime.")
# print("Could not find primes from the test range.")