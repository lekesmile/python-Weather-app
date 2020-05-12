
List = []

while True:
    grade = int(input("Give a course grade (-1 exits): "))
    if grade == -1:
        break
    elif grade > 0 and grade <= 5:
        List.append(grade)
    else:
        print("Grades must be between 1 and 5 (-1 exits)")

avg = sum(List) / len(List)
print("Average of course grades is:", round(avg, 1))

