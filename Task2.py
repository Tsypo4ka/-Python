seconds = int(input("Enter time in seconds: "))

hours = seconds // 3600

seconds %= 3600

minutes = seconds // 60

seconds %= 60

print(f"Time in format: {hours:02}:{minutes:02}:{seconds:02}")
