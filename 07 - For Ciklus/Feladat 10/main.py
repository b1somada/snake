from os import system

kezdoertek: int = None
vegertek: int = None

print("Kérem a kezdő értéket!")
kezdoertek = int(input())

print("Kérem a vég értéket!")
vegertek = int(input())

sum=0

for i in range (kezdoertek,vegertek,1):
    sum = sum + i

print(sum)
