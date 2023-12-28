# No repeatation and 
# There is no definition of order here. prints a different order each time
# unchangable
s = {1,2,4,2,3,6,7,4,3,1}
print(s,type(s))

s2 = {}
print(type(s2))

s3 = set()
print(type(s3))

s4={2,'tias',45,False,9,0,'toki'}
for value in s:
    print(value)
   
for value in s4:
    print(value)
    
#union,intersection of sets 
print(s.union(s4))
print(s.intersection(s4))
# union and update does the same thing except update changes the original set.
s.update(s4)
print(s) 
s.intersection_update(s4)
print(s) 
s5 = {0,2,3,'ellen',1,7,True,None,"zox",23}
# symmetric difference of A and B = (A uniom B) - (A intersection B)
print(s5.symmetric_difference(s4))

# differnce of set A and B is that elements present only in set A or A-B  
print(s5.difference(s4))

# if two sets doesnt have any common element.
print(s.isdisjoint(s5))

# superset and subset
print(s.issuperset(s4))
print(s.issubset(s5))

s6 = {'a','f','g','x'}
s6.add('r')
print(s6)
# discard also does the same. the only difference is that if the element we want to delete is not present in the set remove will throw an error where discard wont.
s6.remove('a')
print(s6)

#randomly deletes and element.
print(s6.pop())
print(s6)

#clear a set
s.clear()
    
        
