#Tuples are used to store multiple items in a single variable. 
# A tuple is a collection which is ordered and unchangeable. 
# Tuples are written with round brackets.

myt = ('apple', 'banana', 'cherry')
print(myt)
print(myt[1])

a=myt.count("banana")
b=myt.index("cherry")
print(a)
print(b)

tup=tuple(("thulasi", "Devops"))
print(tup)
print(tup[0])

tupincomplete=1,
print(tupincomplete)

a,b=1,4
print(a)
print(b)

# tup.clear() # AttributeError: 'tuple' object has no attribute 'clear'
# tup.append("Linux") # AttributeError: 'tuple' object has no attribute 'append

thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)

change=list(thistuple)
change[1]="grapes"
change.remove("cherry")

changetotuple=tuple(change)
print(changetotuple)


#for loop

thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)

#index

thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i],"==",[i])
  
#while loop
thistuple = ("apple", "banana", "cherry")

i=0

while i< len(thistuple):
   print(thistuple[i],"= index value is",[i])
   i = i+1

#Join two tuples:

tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)
