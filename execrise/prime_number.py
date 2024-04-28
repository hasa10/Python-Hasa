#enter the number:7
#7 is prime number
#enter the number:9
#9 is not a prime number
'''number1=input("Enter number:")
number=int(number1)
i=2
while(i<number):
    if number%i==0 :
        print(f'{number} is not prime number')
        break
    if i==number-1:
           print(f'{number} is prime number')
    i+=1




number=10
while number<100:
    i=2
    while(i<number):
        if number%i==0 :
            print(f'{number} is not prime number')
            break
        if i==number-1:
               print(f'{number} is prime number')
        i+=1
    number+=1


rr=0
while rr*rr<=100:
    print(rr*rr)
    rr+=1





name = input('Enter Name:')
len= len(name)
i = 0
while i<len / 2:
    print(name[i] + name[len - i - 1])
    i += 1'''

num = input('Enter number: ')
i = 1
tt = 1
while i <= len(num):
    print(int(num[-i]) * tt)
    tt *= 10
    i += 1













