a = int(input("Enter number: "))
m = a % 10
a = a // 10
while a > 0:
    if a % 10 > m:
        m = a % 10
    a = a // 10
print(f"Max number is {m}!")
