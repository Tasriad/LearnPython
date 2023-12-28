# code a greetings giving clock.
import time
clock  = time.strftime('%H:%M:%S')
print("Present time is:",clock)
hour = int(time.strftime('%H'))
if(hour>0 and hour<5 ):
    print("Why the hell are ya awake!")
elif(hour>5 and hour<12):
    print("Good Morning!")
elif(hour>12 and hour<16):
    print("Good Noon!")
elif(hour>16 and hour<18):
    print("Good Afternoon!")  
elif(hour>18 and hour<19):
    print("Good Evening!") 
else:
    print("Good Night!")                 