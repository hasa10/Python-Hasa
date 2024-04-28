#print only 5 times numbers below than 100
#num=0
#while(num<100):
    #print(num)
    #num=num+5
'''num=0
while(True):

    if(num==100):
        break
    if (num % 5 !=0):
        continue
    print(num)
    num += 5'''


#When teacher enter the marks
#you want to creat a program to print out only more than 50 marks.
#whan teacher finied, she will enter -1
#Enter the marks:60
#60 mark is enterd
#Enter the marks:40
#Enter the marks:70
#60 mark is enterd
#Enter the marks: -1
#finished.

'''while(True):
    marks = int(input("Enter the marks:"))
    if marks.isdigit():
        marks=int(marks)
    else:
        print('Invalid')
    if marks==-1:
        break
    if marks > 50:
        print(f'{marks}is enterd')'''


count=0
while(True):
    love = input("Do you love me?:").upper()
    if love=='NO':
        count+=1
        continue
    if love=='YES':
        print("adarei baba")
        print(f'After{count}years later she gave her word')
        break

















