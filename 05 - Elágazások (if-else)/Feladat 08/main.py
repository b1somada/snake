num: int = None

print("Adjon meg egy számot!")
num = int(input())

if (num % 4 == 0 and num % 6 == 0):
    print("A szám osztható 4-gyel és 6-tal is")
else:
    print("A szám nem osztható 4-gyel és 6-tal is. ")