
def printWords():
    # inputWord = str(input("Give a word:"))
    # ans = input("Print forward? (yes/no): ")
 
   word= input("give word: ")
   decide = input("print forward? (yes/no): ")
   if decide.lower()=="yes":
       print(word)
       i=1
       while i>0:
           wanted = word[i:len(word)+1]
           print(wanted)
           i+=1
           if len(wanted) == 1:
               break
   elif decide.lower()=="no":
       reverse = word[::-1]
       print(reverse)
       j=1
       while j>0:
           wanted2 = reverse[j:len(reverse)+1]
           print(wanted2)
           j+=1
           if len(wanted2) == 1:
               break
   else:
       print("wrong selection: type either yes or no in the decide input")

printWords()