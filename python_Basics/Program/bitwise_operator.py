# 4. Bitwise Operator ===> & , | , ~ , ^
    # 1. & Operator
    # a = 5. and b = 3
    # binary => 1 = True, 0 = False
    #  101
    # &011
    # ----
    #  001  → 1

    # 2. | Operator 
    #  101
    # |011
    # ----
    # 111 → 7
    
    # 3. ^ Operator
    #  101
    # ^011
    # ----
    # 110 → 6
    
    # 4. ~ Operator 
    # a = 5
    # ~a => -(a + 1) = -6
    
    
a = 5
b = 3
print("Bitwise &:", a & b)
print("Bitwise |:", a | b)
print("Bitwise ^:", a ^ b)
print("Bitwise ~a :", ~a)
print("Bitwise ~b :", ~b)



