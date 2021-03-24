#creating a list


cars= list(("Buggati","Mercedes","V8"))
print(cars)

cities=["Nairobi","Mombasa","Kisumu"]
print(cities)
#list can take all datatypes
#consisitency of quotes used


#lists can be nested
games=["Football","Handball","Rugby",[1,2,3],[20.4,56.9]]
print(games)

#example of nestng lists
foods=["Pilau","Chapati","Matoke",[True,False],["Kachori","Chips","Ugali"]]
print(foods)
#one can access an item in a list  
cities=["Nairobi","Mombasa","Kisumu","Nakuru","Kitusuru"]
print(cities[1])
print(cities[2])
print(cities[3])
print(cities[4])

#accessing lists and ranging indexes
cars= list(("Buggati","Mercedes","V8","Subaru","Lambogirni","Tesla"))
print(cars)
print(cars[0])
print(cars[1])
print(cars[2])
print(cars[3])
print(cars[4])
print(cars[5])
print(cars[3:-1])
print(cars[0:])

#check if Item Exists using in keyword
cities=["Nairobi","Mombasa","Kisumu"]
if "Mombasa" in cities:
    print("Yes, 'Mombasa' is in the cities list")
    
games=["Football","Handball","Rugby",[1,2,3],[20.4,56.9]]
if "Rugby" in games:
    print("Yes, 'Rugby' is in the games list")
    
games=["Football","Handball","Rugby",[1,2,3],[20.4,56.9]]
if "Mombasa" in games:
    print("Yes,'Mombasa' is in the games list")
    
    
#changing list items using indexing method
countries=["Kenya","Uganda","Tanzania","Rwanda","Burundi","Congo","Sudan"]
countries[3]="Angola"
print(countries)


#changing list items using insert method
countries=["Kenya","Uganda","Tanzania","Rwanda","Burundi","Congo","Sudan"]
countries.insert(5,"Nigeria")
print(countries)

#changing list items using range method
countries=["Kenya","Uganda","Tanzania","Rwanda","Burundi","Congo","Sudan"]
countries[0:]=["China"]
print(countries)

#changing list items using range method to replace many list items with one item
countries=["Kenya","Uganda","Tanzania","Rwanda","Burundi","Congo","Sudan"]
countries[0:4]=["China"]
print(countries)

#adding list items using append() method
countries=["Kenya","Uganda","Tanzania","Rwanda","Burundi","Congo","Sudan"]
countries.append("Zambia")
print(countries)

#adding list items using append() method
clothes=["Unfinished","Denim","Khaki short","Sweatpant"]
clothes.append("jacket")
print(clothes)

#looping through a list using a for loop
clothes=["Unfinished","Denim","Khaki short","Sweatpant"]
for j in clothes:
    print(j)

#looping through a list using a for loop
clothes=["Unfinished","Denim","Khaki short","Sweatpant"]
for j in clothes:
    print(j)
    
#looping through a list using the range() and len()
clothes=["Unfinished","Denim","Khaki short","Sweatpant"]
for i in range(len(clothes)):
    print(clothes[i])