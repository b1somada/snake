x: int = None
y: int = None
z: int = None

print("Adjon meg 3 számot! (x,y,z)")
x = int(input())
y = int(input())
z = int(input())

if (x % y == 0):
    print("[1] Az X oszható Y-nal")
else:
    print("[1] Az X nem osztható Y-al")

if (x % z == 0):
    print("[2] Az X szám osztható Z-vel")
else:
    print("[2] Az X nem osztható Z-vel")

if (x % z == 0 and x % y == 0):
    print("[3] Az X osztható Y-nal és Z-vel is")
else:
    print("[3] Az X nem oszható Y-nal és Z-vel")