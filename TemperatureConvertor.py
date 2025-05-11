#Temperature Convertor

print("Lucia's Temp Convertor")

Temperature = float(input("Enter a temperature: "))
s_System = input("Is the temp F for Fahrenheit or C for Celsius? ").strip().upper()
s_Degree = chr(176)

# Fahrenheit to Celsius
if s_System == "F":
    if Temperature <= 112:
        f_Celsius = (5.0 / 9) * (Temperature - 32)
        print(f"The Celsius equivalent is: {f_Celsius:.1f}{s_Degree}C")
    else:
        print("Temp cannot be > 112")

# Celsius to Fahrenheit
elif s_System == "C":
    if Temperature <= 100:
        f_Fahrenheit = ((9.0 / 5.0) * Temperature) + 32
        print(f"The Fahrenheit equivalent is: {f_Fahrenheit:.1f}{s_Degree}F")
    else:
        print("Temp cannot be > 100")

# Invalid input
else:
    print("Please enter F or C for the temperature system.")