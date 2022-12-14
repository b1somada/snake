num1: int = None
num2: int = None
type: str = None
result: float = None

import math

print("Kérem az első számot!")
num1 = int(input())
print("Kérem a második számot!")
num2 = int(input())
print("Válaszzon műveletet és írja be a jelét! (+,-,*,/)")
type = str(input())

match type:
    case "+":
        result=num1+num2
        print(f"Ön az összeadást választotta. A végeredmény: {result}")
    case "-":
        result=num1-num2
        print(f"Ön a kivonást választotta. A végeredmény: {result}")
    case "*":
        result=num1*num2
        print(f"Ön a szorzást választotta. A végeredmény: {result}")
    case "/":
        result=num1/num2
        print(f"Ön az osztást választotta. A végeredmény {result}")