name=("hasaranga")
print("a" in name)
if("a" in name):
    print("you are lucky")

print("ha"in name) #True
print("sr"in name) #false
print("as" in name)

print(name[0])
print(name[1])
print(name[5])
#print(name[10])   IndexError: string index out of range
print(name[-1])
print(name[-2])
print(name[0].isdigit())
#name[0]="s"     error
#print('name')
print(name[0].isupper())
#name[0]=name[0].upper()           #TypeError: 'str' object does not support item assignment
print(name[0])
print(name[0:2])
print(name[1:4])
print(name[3:])
print(name[:4])
print(name[-4:-1])
print(name[-4:])
print(name[:-2])
print(name[2:-2])
print(name[:-1])
email=('hvgjhdfcd.com')
print(email[-4:])
print("###",name[-2:-4])
print("@@@",name[3:0])

