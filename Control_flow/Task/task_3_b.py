# 3. Number Comparison

    #1. Check if a number is greater, less, or equal to zero using if–elif–else

    #2. Same logic using nested if

# Method 1
# value = 34

# Method 2
value = int(input("Enter the value of variable :"))

    #  using nested if
if value >= 0:
    if value > 0:
        print(f"The Number {value} is greater than Zero ***")
    else:
        print(f"The Number {value} is Equal to Zero ***")
else:
    print(f"The Number {value} is Less than Zero ***")