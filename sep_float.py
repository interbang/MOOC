number = float(input("Please type in a number: "))
whole = int(number)
if whole >=1:
    tenths = number % whole
if whole <1:
    tenths = number
print(f"Integer part: {whole}")
print (f"Decimal part: {tenths}")