
sentence_file=open("test.txt", "r")
readFile = sentence_file.readlines()
print("The first line in the file is:", readFile[0].strip() )
print("The second line in the file is:", readFile[1].strip() )
print("The third line in the file is:", readFile[2].strip() )
print("The last line in the file is:", readFile[len(readFile)-1])
sentence_file.close()

sentence_file.close()