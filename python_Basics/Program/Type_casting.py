# 12. Type Casting in Python
# 1.Int Conversion
print("*** Int COnversion ***")
# float ===> int
a = 2.4
b = int(a)
print("Float :", a, "  int :", b)

# string ===> int
text = '34'
c = int(text)
print("String:", text, " int :", c)

# boolean ===> int
istrue = True
isfalse = False
d = int(istrue)
e = int(isfalse)

print("Boolean:", istrue, " int :", d)
print("Boolean:", isfalse, " int :", e)
print("\n")
# 2.Float Conversion
print("*** float COnversion ***")
# int ==> float
f = 3
g = float(f)
print("Int :", f, " float :", g)

# string ==> float
h = '2'
i = float(h)
print("String :", h, " float :", i)

# boolean ===> float
t_1= True
f_1 = False

k = float(t_1)
l = float(f_1)
print("Boolean :", t_1, " float :", k)
print("Boolean :", f_1, " float :", l)

print("\n")
# 3.String Converison
print("*** String COnversion ***")
# int ==> string
m = 5
n = str(m)
print("Int :", m, " String :", n)

# float ===> string
o = 3.4
p = str(o)
print("Float :", o, ", String :", p)

# Boolean ==> string
t_2 = True
f_2 = False

q = str(t_2)
r = str(f_2)
print("Boolean :", t_2, " , String :", q)
print("Boolean :", f_2, " , String :", r)

# List ==> string 
my_list = [1,2,3,4, "Hello", True, 3.4]
s = str(my_list)
print("List :", my_list, " , string :", s)
print("\n")

# 4.Boolean Conversion
print("*** Boolean COnversion ***")
# int ==> boolean
t = 0
u = bool(t)
print("Int :", t, " , boolean :", u)

# float ==> boolean
v = 2.3
x = bool(v)
print("Floatt :", v, ", Booolean :", x)

# string ==> boolean
y = "3"
z = bool(y)
print("String :", y, " , Boolean :", z)

# list ==> boolean
lists = [1,2,3,4,5]
bool_c = bool(lists)
print("lists :", lists, " , Boolean :", bool_c)
print("\n")


# 5.List Conversion
print("*** List COnversion ***")

# String ===> List
string_g = "Text Hello World"
li = list(string_g)
print("STring :", string_g, " , list :", li)


# tuple ===> List
tuple_a = (1,2,3)
lis = list(tuple_a)
print("Tuple :", tuple_a, "List :", lis)

# Range ===> List
num = range(10)
list_a = list(num)
print("Range :", num, " , list :", list_a)

print("\n")
# 6.Tuple Conversion
print("*** Tuple Conversion ***")

# List ==> Tuple
list_b = [1,2,3,45,44]
tuple_t = tuple(list_b)
print("List :", list_b, " , tuple :", tuple_t)

# String ==> Tuple
hello = "Hello World !"
tup = tuple(hello)
print("String :", hello, ", Tuple :", tup)


print("\n")
# 7.Set Conversion
print("*** Set Conversion ***")
# list ==> Set

list_abc = [1,2,3,4]
set_a = set(list_abc)
print("List :", list_abc, " , set :", set_a)

# String ==> Set
text_3 = "Hello world this is Python Programming"
set_b = set(text_3)
print("String :", text_3, ", set :", set_b)