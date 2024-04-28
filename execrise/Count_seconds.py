#Time : 12: 55 :34
# a.m or p.m ? am
#______ seconds are over in this day
'''#time=input("Enter time")
what_time=input("Enter am or pm")
x=time.find(":")
y=time.find(":",x+1)
if (time[:x]).isdigit() and (time[x+1:y]).isdigit() and (time[y+1:]).isdigit():
  if int(time[:x])<13 and int(time[x+1:y])<60 and int(time[y+1:])<60:
    if what_time=="am":
        hour=int(time[:x])*3600
        min=int(time[x+1:y])*60
        seconds=int(time[y+1:])*1
        All_seconds=(hour+min+seconds)
        print(f'{All_seconds} seconds are over this day')
    elif what_time=="pm":
        hour=(int(time[:x])+12)*3600
        min=int(time[x+1:y])*60
        seconds=int(time[y+1:])*1
        All_seconds=(hour+min+seconds)
        print(f'{All_seconds} seconds are over this day')

    else:
        print("please enter the am or pm ")
  else:
      print("try again")
else:
    print("try again")'''



#Time : 12: 55 :34
# a.m or p.m ? am
#______ seconds are over in this day
#time=input("Enter time:")
'''what_time=input("Enter am or pm :")
x=time.find(":")
y=time.find(":",x+1)
if (time[:x]).isdigit() and (time[x+1:y]).isdigit() and (time[y+1:]).isdigit():
  if int(time[:x])<13 and int(time[x+1:y])<60 and int(time[y+1:])<60:
    if what_time=="am":
        hour=time[0:x]
        min=int(time[x+1:y])
        seconds=int(time[y+1:])
        print(f'{hour}:{min}h')


    elif what_time=="pm":
        hour=(int(time[:x])+12)
        min=int(time[x+1:y])
        seconds=int(time[y+1:])*1
        print(f'{hour}:{min}h')

    else:
        print("please enter the am or pm ")
  else:
      print("try again")
else:
    print("try again")'''


time=input("Enter the Time(hh:mm:ss):")
if time.count(":")==2:
    find_col1=time.find(":")
    find_col2=time.find(":",find_col1+1)


    hour=time[:find_col1]
    min=time[find_col1+1:find_col2]
    second=time[find_col2+1:]



    if hour.isdigit() and min.isdigit() and second.isdigit():
        am_pm=input("Enter am or pm").lower()

        if int(hour)<=12 and int(min) <60 and int(second)<60:
            if am_pm=="pm":
                hour=hour+12
            second= int(hour)*3600 + int(min)*60 + int(second)
            print(f"{second}seconds are over in this day")

            if len(hour)==1:
                hour='0'+hour
            if len(min)==1:
                min='0'+min
            print(f'{hour}{min}h')



