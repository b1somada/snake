kezdoertek: int = None
vegertek: int = None

print("Kérem a kezdő értéket!")
kezdoertek = int(input())
print("Kérem a vég értéket!")
vegertek = int(input())

if (kezdoertek%2):
        kezdoertek=kezdoertek-1
else:
    None

    for i in range(vegertek,kezdoertek,-2):
        print(i)




