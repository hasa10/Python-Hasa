#Enter decimal number:20.456
#there are 3 decimals
#Use len(number) & string.find
num=input("Number:")
dec_po=num.find(".")

if dec_po != -1:
    if (num.count("."))==1:
        if num[:dec_po].isdigit() and num[dec_po+1:].isdigit():
            num_dec = len(num) - dec_po - 1
            print(f"There are {num_dec} decimal")
        else:
            print("Use only digits")

    else:
        print("invalid number")

else:
    print("There are no decimals")
    