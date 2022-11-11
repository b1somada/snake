num: int = None

print("Adjon meg egy számot!")
num = int(input())

if (num>=10 and num<=20):
    print("A szám 10 és 20 között van.")
elif (num < -10 and num > -20):
    print("A szám -10 és -20 között van.")
else:
    print("A vizsgált szám nem felelt meg a feltételeknek.")