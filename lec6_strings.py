# Strings are immutable
s1 = "MaiZers"
print(len(s1))
print(s1.upper())
print(s1.lower())

s2 = "Tias!!!!!!!"
print(s2)
print(s2.rstrip("!")) # gets rid of trailing characters

s3 = "Tias is the best. Tias is goated. Everyone likes Tias."
print(s3)
print(s3.replace("Tias","Tias's wife"))

s4 = "fire,water,wind,earth,lightning,holy,darkness"
element_list = s4.split(",")
for element in element_list:
    print(element)
    
s5 = "heAdiNg"  
print(s5.capitalize())

s6 = "Maximum" 
print(s6.center(20)) # (n-len)/2 spaced

print(s3.count("Tias"))

s7 = "tias is, awesome!"
print(s7.endswith("!"))
print(s7.endswith(",",2,8))

s8 = "Everyday is boring. There is nothing for Tias to do."
print(s8.find("Tias"))
print(s8.find("yo"))
# print(s8.index("yo"))

s9 = "Sup bro!"
s10 = "Sup bro"
s11 = "Sup bro9"
print(s9.isalnum()) # alphanum = a-z,A-Z,0-9
print(s10.isalnum())
print(s11.isalnum())
print(s9.isalpha()) # alpha = a-z,A-Z
print(s10.isalpha())
print(s11.isalpha())

s12 = "alter ego is the ego of alterism."
print(s12.startswith("alter"))

# s12.islower()
# s12.isupper()
# s12.istitle()
# s12.isprintable()
# s12.isspace()

s13 = "YoFuCk"
print(s13.swapcase())