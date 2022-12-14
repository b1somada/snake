R1: int = None
R2: int = None
type: str = None
vegeredmeny: float = None

import math

print("Kérem az R1 értékét!")
R1 = int(input())

print("Kérem az R2 értékét!")
R2 = int(input())

print("Párhuzamos (P) vagy Soros (S) kapcsolás?")
type = str(input().lower().strip())

match type:
    case "p":
        vegeredmeny=(R1+R2)/(R1*R2)
        print(f"Párhuzamos kapcsolás esetén az eredő ellenállás: {vegeredmeny}")
    case "s":
        vegeredmeny=R1+R2
        print(f"Soros kapcsolás esetén az eredő ellenállás: {vegeredmeny}")