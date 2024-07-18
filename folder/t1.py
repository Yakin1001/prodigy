try:
    value = float(input("Enter the temperature value: "))
    unit = input("Enter the unit of measurement (C, F, K): ").upper()
    
    if unit == 'C':
        fahrenheit = (value * 9/5) + 32
        kelvin = value + 273.15
        print(f"{value}°C is {fahrenheit:.2f}°F and {kelvin:.2f}K")
    elif unit == 'F':
        celsius = (value - 32) * 5/9
        kelvin = (value - 32) * 5/9 + 273.15
        print(f"{value}°F is {celsius:.2f}°C and {kelvin:.2f}K")
    elif unit == 'K':
        celsius = value - 273.15
        fahrenheit = (value - 273.15) * 9/5 + 32
        print(f"{value}K is {celsius:.2f}°C and {fahrenheit:.2f}°F")
    else:
        print("Invalid unit. Please enter C for Celsius, F for Fahrenheit, or K for Kelvin.")
except ValueError:
    print("Invalid input. Please enter a numeric value for the temperature.")