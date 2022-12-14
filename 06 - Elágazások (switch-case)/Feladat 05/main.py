x: int = None
y: int = None
result: str = None
vegeredmeny: float = None

print("Kérem a két ellenállás értékét!")
x = int(input())
y = int(input())

print("Adja meg a kötést! (P = párhuzamos , S = soros)")
result = str(input().upper().strip())

match result:
    case "P":
        vegeredmeny = (x+y)/(x*y)
        print(f"Eredő ellenállás: {vegeredmeny}")
    case "S":
        vegeredmeny = x+y
        print(f"Eredő ellenállás: {vegeredmeny}")