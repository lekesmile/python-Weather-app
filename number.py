from statistics import mean

readNum = open("numbers.txt", "r")
arrayNumbers = readNum.readlines()

f = list(map(int, arrayNumbers)) # Map to set array elements into int

print("Lowest number in the file was", min(f))
print("Highest number in the file was", max(f))
print("Average of all numbers is", round(mean(f), 1))
readNum.close()