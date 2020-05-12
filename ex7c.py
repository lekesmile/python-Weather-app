
ListName = {}



while True:

   print("Phone book ver. 1.0.1")
   case1 = print("1) Add new number to the directory")
   case2 = print("2) Search for a contact")
   quitCase = print("0) Quit")
    
   question = input("What would you like to do?: ") 
   if question == "0":
      break
   elif question == "1":
        name = input("Give the name for the new contact: " )
        phone = input("Give the number for the new contact: ")
        phoneObject = {name:phone}
        ListName.update(phoneObject)
   else:
       searchName = input("Input the name you want to search in the directory: ")
       print("Number for " + searchName + " is " + ListName.get(searchName) )




