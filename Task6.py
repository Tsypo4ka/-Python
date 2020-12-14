a = int(input("Enter first day km: "))
b = int(input("Enter last day km: "))
i = 1
while True:
    if a < b:
        i = i + 1
        a *= 1.1
        print(f"{a:.2f}")
    if a >= b:
        break
print(f"He needs {i} days!")
