def printer(word):
    for i in range(len(word)):
        print(word[i:])


text = input("Give a word: ")
forward = input("Print forward? (yes/no): ")


if forward=="no":
    printer(text[::-1])
else:
    printer(text)
