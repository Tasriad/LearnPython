# tuples are not changable 
tup = (1,3,2,6,4,8,6,7,6)
print("initial tuple tup:",tup)
# tup[0] = 4 this is not allowed
print("0th index of tup:",tup[0])
print("-1th index of tup is length(7)-1 tup[6]:",tup[-1])

#slicing
tup2 = tup[1:6:2]
print("from index 1 to index 5 jumps 2 steps so tup2:",tup2)

#merege
tup3 = tup + tup2
print('tup3 is the merge of tup1 and tup2:',tup3)

#count occurence 
print("occurence of 6:",tup.count(6))

#index of
print("first index of 6 from index 4 to 8:",tup.index(6,4,8))
