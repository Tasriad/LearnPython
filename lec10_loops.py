list = ['red','blue','green','yellow','orange','black','white']
for color in list:
    print("\n")
    print(color)
    for letter in color:
        print(letter,end=",")


print("\n")        
for i in range(10):  # 0 to n-1
    print(i)
print("\n")      
for i in range(3,10):
    print(i)
print("\n")
for i in range(0,10,2):
    print(i)  


print("\n")
i=1
while(i<100):
    print(i)
    i*=2 

# emulating do while loop
i=1
while True:
    print(i)
    if(i%10==0):
        break
    i+=1
                                   