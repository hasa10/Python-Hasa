#Enter Name: Hasaranga
#middle letter is "r"

#Enter name:Shehan
#middle Letter is "eh"
name=input("Enter Name:")
if (len(name)%2==1):
    print("len(name)%2",len(name)%2)
    print("len(name):",len(name))
    print("len(name):/2",len(name)/2)
    print("int(len(name)/2",int(len(name)/2))
    middle=int(len(name)/2)
    print(name[middle])
else:
    print("len(name)%2",len(name)%2)
    print("len(name):",len(name))
    print("len(name):/2",len(name)/2)
    print("int(len(name)/2",int(len(name)/2))
    middle=int(len(name)/2)
    print(name[middle-1:middle+1])







