
sentences = open("sentences.txt", "r")
f = sentences.readlines()
for i in f:
    print(i.strip(), "=>" , i.upper().strip() )


sentences.close()