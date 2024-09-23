# patern drawing app
number = int(input("Enter the size of the pattern: "))
c = 1

while c <= number:
    for i in range(number) :
        print("*", end="")
    print()
    c += 1