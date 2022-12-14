drink: str = None

print("Válasszon üdítőt!")
drink =str(input())

match drink:
    case "Coca-Cola":
        print("Választott ital: Coca-Cola")
    case "Pepsi":
        print("Választott ital: Pepsi")
    case "Fanta":
        print("Választott ital: Fanta")
    case "Sprite":
        print("Választott ital: Sprite")