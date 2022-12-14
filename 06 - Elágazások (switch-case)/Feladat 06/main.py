length: int = None
width: int = None
result: str = None
vegeredmeny: float = None
reszeredemeny: int = None

import math

print("Kérem a téglalap hosszát, majd a szélességét!")
length = int(input())
width = int(input())

print("(t - terület , k - kerület , a - átló) Írja be a betűjelét a választott műveletnek!")
result = str(input())

match result:
    case "k":
        vegeredmeny = 2*(length+width)
        print(f"Kerület: {vegeredmeny}")
    case "t":
        vegeredmeny = length*width
        print(f"Terület: {vegeredmeny}")
    case "a":
        reszeredemeny = length**2 + width**2
        vegeredmeny = math.sqrt(reszeredemeny)
        print(f"Átló hossza: {vegeredmeny}")