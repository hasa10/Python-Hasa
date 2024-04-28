# palindrome number : 131, 1441, 27972, 4567654
# Find all the palindrome numbers 100 and 10000 and count it.

pal=100
count=0

while (pal<10000):
    pal += 1

    pal2= str(pal)
    if pal2[::-1] == pal2[0::]:
        count += 1
        print(pal)
        print(count)
    else:
        continue






