name="hello alle"
cap="HELLO ALL"
swap="hElLo aLl"

print(name.upper())
print(cap.lower())
print(name.title())
print(cap.title())
print(name.capitalize())
print(name.swapcase())
print(swap.swapcase())

print(name.isupper())
print(name.islower())
print(name.istitle())


print(name.index("l"))
print(name.rindex("a")) #if the substring is not found it will throw an error
print(name.find("h")) #if the substring is not found it will return -1
print(name.rfind("l"))
print(name.count("l"))
print(name.startswith("h"))
print(name.endswith("l"))
print("length:",len(name))

mail="thulasira@gmail.cm"

if mail.find("@") !=-1:
    print("valid email")
if mail.endswith(".com"):
    print("valid email")
else: print("invalid email")