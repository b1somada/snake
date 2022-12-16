from os import system

kezdoertek: int = None
vegertek: int = None

print("Kérem a kezdő értéket!")
kezdoertek = int(input())

print("Kérem a vég értéket!")
vegertek = int(input())

paros=0
paratlan=0

for i in range(kezdoertek,vegertek,1):
    print(i)
if (i % 2):
    paros+i
else:
    paratlan*i

print(paratlan)
print(paros)