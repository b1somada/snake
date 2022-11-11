num1: int = None
num2: int = None

print("Adja meg az első számot!")
num1 = int(input())

print("Adja meg az első számot!")
num2 = int(input())

if (num1<num2):
    print(f"A nagyobb szám: {num2}")
else:
    print(f"A nagyobb szám: {num1}")