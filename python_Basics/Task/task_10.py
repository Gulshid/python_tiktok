# 10. Write a Program for Making Student Subject Calculator
# Method 1
# eng = 80
# urdu = 87
# computer = 77
# chem = 78
# phy = 80
# bio = 89

# Method 2
eng = int(input("Enter the English Marks :"))
urdu = int(input("Enter the urdu Marks :"))
computer = int(input("Enter the computer Marks :"))
phy = int(input("Enter the phy Marks :"))
chem = int(input("Enter the chem Marks :"))
bio = int(input("Enter the Bio Marks :"))


print("*** Student Subjects  ***")
print(f"Eng : {eng},   urdu : {urdu} ,    Computer : {computer}")
print(f"Phy : {phy},   Chem : {chem} ,    Bio : {bio}")

print("*** Subject total Marks ***")
total = eng + urdu + computer + phy + chem + bio
print("Total Marks :",total )
