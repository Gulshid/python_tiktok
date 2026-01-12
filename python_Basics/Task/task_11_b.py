# 11. How to Swap two Number with and Without third Variable
# Without third Variable Method 
a = 30
b = 40

print("*** Before Swapping Values ***")
print(f"The value of a : {a} , and the value of b is : {b}")


a = a + b # a = 70
b = a - b # b = 30
a = a - b # a = 40

print("*** After Swapping Values ***")
print(f"The value of a : {a} , and the value of b is : {b}")