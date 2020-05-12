
add = 1
openFloat = open("floats.txt", "r")
arrayFloat = openFloat.readlines()

f = list(map(float, arrayFloat))

print(arrayFloat)
print("The sum of all numbers was:", round(sum(f), 2))
for i in arrayFloat:
    add += len(str(i[:-2].strip()))
print("The amount of numeric symbols in the file was:", add)
openFloat.close()