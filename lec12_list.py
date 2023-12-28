numbers = [1,3,4,6,8,9,0]
print("initial numbers list:",numbers)
if 5 in numbers:
    print("Yes 5 in numbers")
else:
    print("No 5 is not in numbers")

    
print("starts from index 0 goes to index 4.jumps 2 step each time.")   
print(numbers[0:5:2])  # jump index is 2


list = [i for i in range(10)]
list2 = [i for i in range(20) if i%2==0]
print("list using range 10:",list) 
print("list using range 20 but only even:",list2) 


l = [1,5,8,3,9,2]
print("list l:",l)
# reverse
print("reverse of the list l:")
l.reverse()
print(l)
# sort ascending
print("sorting of the list l in ascending:")
l.sort()
print(l)
# sort descending
print("sorting of the list l in descending:")
l.sort(reverse=True)
print(l)
# first index of 2
print("first index of 2:",l.index(2))
# append
print("appending 3")
l.append(3)
print(l)
# inserts 3 at index 1
l.insert(1,3)
print("nserts 3 at index 1")
print(l)
# occurence of 3
print("occurence of 3:",l.count(3))
# assigns reference
m=l
m[0] = 0
print("if m=l then changing m will also change l")
print(l[0])
print(m[0])
# assigns copy
m=l.copy()
m[1] = 1
print("if m=l.copy() then changing m will not change l")
print(l[1])
print(m[1])
# appends m to l
m=[100,200,300]
print("list m:",m)
print("list l:",l)
print("appending m to l:")
l.extend(m)
print(l)
    