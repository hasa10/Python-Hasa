#if number of month is 4 'This month has 30 days'
#if number of month is 3 'This month has 31 days'
#if number of month is 12 'This month has 31 days'
#if number of month is 11 'This month has 30 days'
#if number of month is 2 'This month has 28'
print('Enter the month:',end='')
month = 2
print('Enter the year:',end='')
year=2020
month=8
print(f'Enter the year:{year}')
print(f'Enter the month: {month}')
if month<=12:
    if year%4==0:
        print('february has 29 days')
    elif month ==2:
        print('This month has 28')
    elif month<8:
        if month % 2==0:
            print('This month has 30 day')
        else:
            print('This month has 31 day')
    else:
        if month %2 ==1:
            print('This month has 30 day')
        else:
            print('This month has 31 days')
else:
    print('invalid number')


