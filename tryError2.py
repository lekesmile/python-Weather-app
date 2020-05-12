

name = input("Give name for the file: ")

try:
    with open(name, "r") as infile:
        print("Succesfully opened", name, "reading contents...")

        for r in infile:
            print(r[:-1])

except:
    print("Could not open", name)