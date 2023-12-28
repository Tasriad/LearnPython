'''
multi 
line 
comment
'''
print("Hello world! I am Tias.")
print("the number",5,"and",7) #auto space
print(6/5)
print(6//5) #floor division
print(3**2)
print("hey i am a \"good boy\".\nevery girl wants my seed.")
print("hey",5,"yo",6,sep="/ ",end=" over\n")
print("starting new line")
poem = '''
O my night! I thy so you love me for the "strap". can you hear me the song of life that,'hither the song'
O sun the moon star will rise 
the cat will dance ,
/since the fire.
'''
# multi line string
print(poem)
str1 = "Tias"
print(str1[2])
#length of string
print(len(poem))
# slicing of string (prints from start to end -1)
print(str1[1:3])
print(poem[0:10])
print(poem[-123:-118]) # negative slicing means len(string) - n
str2 = "Harry"
print(str2[-4:-2])
# for each loop
for char in str1 :
    print(char)