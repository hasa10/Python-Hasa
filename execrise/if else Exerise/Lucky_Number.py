#Enter Your Birth Date : 1895/06/22
#Your Lucky Number is : 6
# Calculation part : 1+8+9+5+0+6+2+2+=43
#then, 4+3 =7
# You can use replace method
#Use while
#lucky_number +=......[variable]

'''birth_date = input('Enter Your Birth Date (yyyy/mm/dd):')
number = birth_date.replace("/", "")
lucky_number = 0
lucky_number2 =0
while number:
    lucky_number += int(number[0])
    number = number[1:]
lucky = str(lucky_number)

while lucky:
    lucky_number2 += int(lucky[0])
    lucky = lucky[1:]
lucky2 = str(lucky_number2)
print(f'Your Lucky Number is: {lucky2}')'''

date = input('Enter Your Birth Date (yyyy/mm/dd):')
if date.count('/')==2:
    date=date.replace("/","")
    if(date.isdigit()):
        while (True):
            index = 0
            lucky_number = 0
            while (index < len(date)):
                lucky_number += int(date[index])
                index += 1
            date = str(lucky_number)
            if len(date) == 1:
                break
        print(date)





















