num: int = None

print("Adjon meg egy számot!")
num = int(input())

if (num >= 0 and num<=9):
    print("A szám 0 és 9 között van")
elif (num >= 10 and num <= 99):
    print("A szám 10 és 99 között van")
else:
    print("A szám 100 és 999 között van")