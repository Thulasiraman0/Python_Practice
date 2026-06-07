"""
================================================================================
                    PYTHON LISTS - COMPREHENSIVE TUTORIAL
================================================================================
Lists are mutable (changeable) collections that can store multiple data types.
Key characteristics:
- Ordered: Elements maintain their position
- Mutable: Can be modified after creation
- Indexed: Access elements using position (0-based indexing)
- Heterogeneous: Can store different data types
================================================================================
"""

""" #colllection
#list mutable dataaa type

list=['thulasi','raman']
print(list)

print(list[0])
a=list[1]="Devops"

print(a)
print(list)

new=list.append("Engineer")
print(list)

newsalary=list.append(50000)
print(list)

print(len(list))


print(list[0:2])

print(list[-3:-1])
print(list[-1:-3:-1])
print(list[-2:])
print(list[0:3:2])
print(list[::2])
"""

my_list = ['thulasi', 'Devops', 'Engineer', 50000]
'''new_list = my_list[::-1]
print(new_list)  # Output: [50000, 'Engineer', 'Devops', 'thulasi']

rev=list(reversed(my_list))
print(rev)

my_list.reverse()
print(my_list)
'''



#methods

my_list.append("Linux")
print(my_list)
 
print(my_list.count("Devops"))
print(my_list.index(50000))
my_list.insert(1, "Windows")
print(my_list)
print(my_list.index(50000))
my_list.pop(4)
print(my_list)

my_list.pop()
print(my_list)


l=[1,2,3,5,2,1,4,6,3,8,3,4,3,2]
'''l.pop()
print(l)

a=l.pop()
print(a)
print(l)
'''
l.reverse()
print("rev:",l)
l.sort()
print("sort:",l)

l.sort()
print(l)

list1 = [1, 2, 3]

list1.clear()
print(list1)

print(len(list1))


squares=[x**2 for x in range(1,11)]
print("squares:",squares)

even=[x for x in range(1,11) if x%2==0]
print("Even:", even)

even_squares=[x**2 for x in range(1,11) if x%2==0]
print("Even squares:", even_squares)

u=[x.upper() for x in my_list]
print(u)

lower=[x.lower() for x in my_list if isinstance(x, str)]
print(lower)

