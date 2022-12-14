kezdo: int = None
veg: int = None

print("Kérem a kezdő értéket!")
kezdo = int(input())
print("Kérem a vég értéket!")
veg = int(input())

for i in range(kezdo,veg,-1):
    print(i)