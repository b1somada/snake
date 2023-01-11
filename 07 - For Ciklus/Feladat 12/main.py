from os import system

kezdoertek: int = None
vegertek: int = None
vegeredmeny: int = None

print("Kérem a kezdőértéket!")
kezdoertek = int(input())

print("Kérem a végértéket!")
vegertek = int(input())

for i in range(kezdoertek,vegertek,1):
    if (i % 3):
        vegeredmeny=vegeredmeny+1
    else:
        vegeredmeny=vegeredmeny+0

print(vegeredmeny)