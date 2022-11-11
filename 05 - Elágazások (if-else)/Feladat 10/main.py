num: int = None

print("Adjon meg egy számot!")
num = int(input())

if (num % 2 == 0):
    print("BIZ")
else:
    print("")

if (num % 3 == 0):
    print("BAZ")
else:
    print("")

if (num % 3 == 0 and num % 2 == 0):
    print("ZIZI")
else:
    print("")


