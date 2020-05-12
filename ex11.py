

import csv


userInput = input("Give name of the csv file containing song lyrics: ")
if userInput == "taylor_swift_lyrics.csv":
     searchWord = input ("Give a word or a phrase to search from the lyrics: ")
     with open("taylor_swift_lyrics.csv", "r") as lyricsfile:
         reader = csv.reader(lyricsfile)
         for row in reader:
             if row[4].find(searchWord) != -1:
               newR = (row[4])
               if newR.find(",") == -1:
                   print(newR)
else:
    print("Cannot find your requested file")


