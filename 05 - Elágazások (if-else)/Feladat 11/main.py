num: int = None

print("Adjon meg egy számot!")
num = int(input())

if (num > 0):
    print("[1] A szám pozitív")
else:
    print("[1] A szám negatív")

if (num % 2 == 0):
    print("[2] A szám páros")
else:
    print("[2] A szám páratlan")

if (num % 5 == 0):
    print("[3] A szám osztható 5-tel")
else:
    print("[3] A szám nem osztható 5-tel")