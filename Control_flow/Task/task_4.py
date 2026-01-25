# 4. Reverse Display

    # 1.Display a list or number series in reverse order
    
value = int(input("Enter the Series number :"))

reverse = 0

while value > 0:
    digit = value % 10
    reverse = reverse * 10 + digit
    value = value // 10
    
print("Reverse Series :", reverse)