receipt = int(input("Enter your receipt: "))
cost = int(input("Enter your cost: "))

if receipt > cost:
    print("Profit!")
    rent = receipt / cost
    print(f"Profitability is {rent:.2f}")
    staff = int(input("Enter the number of staff: "))
    profit1 = (receipt - cost) / staff
    print(f"firm's profit per one staff: {profit1:.2f}")
if receipt < cost:
    print("You are loss!")
if receipt == cost:
    print("You are in ZERO!")
