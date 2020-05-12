
List = []

while True:
    shoppingList = input("Add new item to shopping list: ")
    if shoppingList == '0':
        break
    else:
        List.append(shoppingList)
print("Items on your shopping list are: ")
for items in List:
    myList= ", ".join(List)
print(myList)