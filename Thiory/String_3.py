name="Hasaranga"
print(name.index("a"))
print(name.index("a",0,3))
print(name.index("a",-3))
print(name.index("a",3,6))
print(name.index("a",2,-2))
#print(name.index("Z"))      ValueError: substring not found
print('find')
print(name.find("a"))    #1
print(name.find("a",3,6))    #3
print(name.find("z"))    #-1
print(name.find("r"))     #4
print(name.count("a",0,5))  #2
print(name.count("a"))       #4
print(name.replace('a','u',2))   #Husuranga
print(name.replace("a","",1))      #Hsaranga
print(name.replace("a",""))    #Hsrng
print(name.replace("a","zz",))  #Hzzszzrzzngzz
print(name.replace("as","bc"))     #Hbcaranga
print(name.replace("z","a",1)) #Hasaranga
full_name='RasithaHasaranga'
print(full_name.isspace())#False
print(not full_name.isspace())#True
print(name.removeprefix("H"))    #asaranga
print(name.removeprefix("Has"))  #aranga
print(name.removesuffix("a"))    #Hasarang
print(name.removesuffix("ga"))#Hasaran
print(name.removesuffix("r"))  #Hasaranga

print(name[::-1])