while True:

    print("Please choose a start value, end value and a set increment")
    
    x = int(input("Starting Value: "))

    y = int(input("Ending Value: "))

    z = int(input("Increment: ")) 

    for number in range(x, y, z):
        print(number)
    print()