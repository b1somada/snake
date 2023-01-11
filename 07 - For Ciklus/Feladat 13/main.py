kezdoertek: int = None
vegertek: int = None
paros: int = None
paratlan: int = None

print("Kérem a kezdőértéket!")
kezdoertek = int(input())

print("Kérem a végértéket!")
vegertek = int(input())

for i in range(kezdoertek,vegertek,1):
    if (i % 2):
        paros+i
    else:
        paratlan+i

print(paros)
print(paratlan)