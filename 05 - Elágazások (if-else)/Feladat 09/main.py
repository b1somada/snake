x: int = None
y: int = None

print("Adja meg az X értékét!")
x = int(input())

print("Adja meg az Y értékét!")
y = int(input())

if (x % y == 0):
    print(f"Az {y} osztója ennek: {x}")
else:
    print("Nem oszhtója a két szám egymásnak")