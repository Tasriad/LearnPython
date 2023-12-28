introduction = "Hey I am {}. And I am from {}."
name="Tias"
country="Bangladesh"
print(introduction.format(name,country))

introduction2 = "Hey I am {1}. And I am from {0}."
print(introduction2.format(country,name))

# f string
print(f"Hey I am {name}. And I am from {country}.")
# it will round
price = 45.678999
print(f"You can buy it for only {price:.2f} taka") 
#you can use valid python expression
print(f"{2*30}")
#show the {}
print(f"Hey I am {{name}}. And I am from {{country}}.")
