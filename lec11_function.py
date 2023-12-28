def average(list):
    n=len(list)
    sum=0
    for i in list:
        sum+=i
    avg = sum/n
    return avg
def GeoAvg(list): #pass means skip
    pass
#variable length argument
def average2(*numbers):  # taken as a tuple
    sum=0
    for i in numbers:
        sum+=i
    return(sum/len(numbers)) 
def name(**name):  #taken as dictionary
    print("Hello",name["fname"],name["mname"],name["lname"])
       

l1 = [2,5,7,9,8,12]
print(average(l1))
print(average2(2,5,7,9,8,12)) 
name(fname="Tasriad",mname="Ahmed",lname="Tias")   