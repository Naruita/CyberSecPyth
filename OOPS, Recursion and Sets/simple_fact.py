def fact(number):
    if number == 1:
        return number
    return number*fact(number-1)

print(fact(int(input("Enter the number : "))))