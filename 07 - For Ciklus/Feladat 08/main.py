kezdoertek: int = None
vegertek: int = None

print("Kérem a kezdő értéket!")
kezdoertek = int(input())
print("Kérem a vég értéket!")
vegertek = int(input())

if (kezdoertek % 2):
    kezdoertek-1
else:
    None

for i in range(kezdoertek,vegertek,2):
    print(i)