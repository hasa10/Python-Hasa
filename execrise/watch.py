''''#1 weni prashnaya
num2=1
while(num2<=5):
    num=1
    while(num<=5):
        print(num2,end=" ")
        num+=1
    print()
    num2+=1



#2 weni prashnaya
num=1
while num<=50:
    tt=1
    hh=1
    while(num >= hh):
        print(num,end=" ")
        hh+=1
    print()
    num+=1



#3weni prashnaya
num=1
while num<=60:
    tt=1
    hh=1
    while(num >= hh):
        print(hh,end=" ")
        hh+=1
    print()
    num+=1


#4 weni prashnaya
num=1
while num<=5:
    tt=1
    hh=1
    while(num >= hh):
        print(hh,end=" ")
        hh+=1
    print()
    num+=1

num2 =4
while num2 >= 0:
    hh =1
    tt=num2
    while  tt>=hh:
        print(hh,end=" ")
        hh+=1
    print()
    num2-=1



hour = 12
while (hour<14):
    min=0
    while (min<60):
        sec=0
        while (sec<60):
            minutes=min
            seconds=sec
            if minutes<10:
                minutes='0'+str(minutes)
            if (min<10) and (sec<10):
                print(f'{hour}:0{min}:0{sec}')
            elif (min<10):
                print(f'{hour}:0{min}:{sec}')
            elif (sec<10):
                print(f'{hour}:{min}:0{sec}')
            else:
                print(f'{hour}:{min}:{sec}')

            sec+= 1
        min+= 1
    hour+= 1


rr=1
hh=10
while (rr<=hh):
    spa= ' ' * (hh - rr)
    sta = ' *' * rr
    print(spa + sta )
    rr +=1


rr=1
hh=100
while (rr<=hh):
    spa= " " * (hh - rr)
    sta = ' *' * rr
    print(f'{spa}{rr}{sta} ')
    rr +=1


rr=1
hh=10
while (rr<=hh):
    spa= ' ' * (hh - rr)
    sta = ' *' * rr
    print(spa + sta )
    rr +=2
tt=0
while (tt<7):
    spa2=' ' * 7
    sta2=' *' *3
    print(spa2+sta2)
    tt+=1

rr = 1
hh =13
gg=4
while rr <= hh:
    spa2 = ' ' * gg
    spa = ' ' * (hh - rr)
    sta = ' *' * rr
    print(spa2+spa + sta)
    rr += 2

rr =10
hh = 15
gg=2

while rr <= hh:
    spa2=' '*gg
    spa =' ' * (hh - rr)
    sta = ' *' * rr
    print(spa2+ spa + sta)
    rr += 2
rr = 10
hh = 15
gg=2
while rr <= hh:
    spa2 = ' ' * gg
    spa = ' ' * (hh - rr)
    sta = ' *' * rr
    print(spa2+spa + sta)
    rr += 2

tt = 0
while tt < 7:
    spa2 = ' ' *13
    sta2 = ' *' * 4
    print(spa2 + sta2)
    tt += 1'''







gg=50
dd=0
hh = 10

while (dd<3):
    rr = 1
    while rr <= hh:
        spa2 = ' ' * gg
        spa = ' ' * (hh - rr)
        sta = ' *' * rr
        print(spa2+spa + sta)
        rr += 2
    dd +=1
    hh+=4
    gg-=4

tt = 0
while tt < 7:
    spa2 = ' ' *56
    sta2 = ' *' * 4
    print(spa2 + sta2)
    tt += 1


