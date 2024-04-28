#if he was born after 2000, he is stubborn,otherwise he is obedient
date =input("Enter your birth date:(yyyy/mm/dd):")
#if he is born in 9 month,he is unlocky.
if (date.count("/"))==2:
    first_slash = date.find('/')
    second_slash = date.find('/',first_slash + 1)
    if date[:first_slash].isdigit() and date[first_slash + 1:second_slash].isdigit() and date[second_slash + 1:].isdigit():
        if len(date[:first_slash]) == 4 and int(date[first_slash + 1:second_slash]) < 13 and int(date[second_slash + 1:]) < 33:
            if int(date[first_slash + 1:second_slash])== 9:
                print('You are unlucky')
            else :
                print('You are lucky')
            if int(date[:first_slash])>= 2000:
                print('You are stubborn')
            else:
                print('You are obedient')



