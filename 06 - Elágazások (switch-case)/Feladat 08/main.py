length: int = None
width: int = None
type: str = None
reszeredmeny: float = None
vegeredmeny: float = None

import math

print("Kérem a télglalap hosszát!")
length = int(input())

print("Kérem a téglalap szélességét!")
width = int(input())

print("Válasszon műveletet! (T - terület , K - kerület , A - átló)")
type = str(input().lower().strip())


match type:
    case "t":
        vegeredmeny=length*width
        print(f"A téglalap területe: {vegeredmeny}")
    case "k":
        vegeredmeny=2*(length+width)
        print(f"A téglalap kerülete: {vegeredmeny}")
    case "a":
        reszeredmeny=length**2+width**2
        vegeredmeny=math.sqrt(reszeredmeny)
        print(f"A télgalap átlójának hossza: {vegeredmeny}")