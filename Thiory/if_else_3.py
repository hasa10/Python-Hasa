if 7>6 and 5>4 :
    print('and')
if 7>6 and 8>9 :
    print('and2')  #dekama hari giyoth witharai pennanne
if 8>9 and 5>3 :
    print('and3')
if 6>7 and 7>9 :
    print('and4')

if 7>6 or 5>4 :
    print('or')
if 7>6 or 8>9 :
    print('or2')
if 8>9 or 5>3 :       # ekak hari giyoth witharai pennanne
    print('or3')
if 6>7 or 7>9 :
    print('or4')

if not 7==3 :
    print('not1')
if not 7>3 :
    print('not2')   # hari nam pennanne na  weradinam pennanawa

if 7>6 and 8>5 and 4>2 :
    print('3*and')
if 7>6 or 8>5 or 4>2 :
    print('3*or')
if  7>6 and 8>5 and 1>2 :
    print('and, 2 True')
if  7>6 or 8>5 or 1>2 :
    print('or, 2 True')
if  7>6 and 8>5 or 1>2 :
    print('and=True or false')
if  7>6 or 8>5 and 1>2 :
    print('or = True and False')
if  7>8 and 8>5 or 1>2 :
    print('and=false or True')
if 7>8 or 8>5 and 1>2 :
    print('or=True or True')
if 7>8 and 8>5 or 1>2 :
    print('and=True or false')
if not 7>8 or 8>5 and not 5>2 :
    print('or=True and not True')
if not 7>8 and 8>5 and 5>2 :
    print('not false,and True and true')

if 7==8 and 7>8 or 4==4:
    print('false and false or true')
if 7==8 and 7>8 or 4==4:
    print('false and (false or true) =false')
if 7>8 or (8>5 and 1>2) :
    print('false or ( True and False = False)')
if 7>8 and 4>2 or 1>2 and 5>2:
    print('False and True = False, false or True= True,True and True=True')
if (7>8 and 4>2) or (3>2 and 5>2):
    print('False or True = True')
