# 13 Write a Program for Conversion of Celsius and Fahrenheit with each Other
print("*** Tempreture Conversion ***")


Fahrenheit = float(input("Enter the fahrenheit :"))
Celsius = (Fahrenheit - 32) * 5/9
print("*** Fahrenheit to Celsius Conversion ***")
print(f"The Celsius of {Fahrenheit} is : {Celsius}")


print("*** Celsius to Fahrenheit Conversion ***")
Celsius = float(input("Enter the Celsius :"))
Fahrenheit = (Celsius * 9/5) + 32
print(f"The Fahrenheit of {Celsius} is : {Fahrenheit}")