x: int = None
y: int = None
eredmeny: float = None
muvelet: str = None

print("Adja meg az első számot!")
x = int(input())

print("Adja meg a második számot!")
y = int(input())

print("Adja meg a műveletet! (+,-,*,/)")
muvelet = str(input())

match muvelet:
    case "+":
        eredmeny = x + y
        print(f"Az eredmény: {eredmeny}")
    case "-":
        eredmeny = x - y
        print(f"Az eredmény: {eredmeny}")
    case "*":
        eredmeny = x * y
        print(f"Az eredmény: {eredmeny}")
    case "/":
        eredmeny = x / y
        print(f"Az eredmény: {eredmeny}")