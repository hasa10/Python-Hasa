i =0
while (i<7):
    print(i)
    i+=1

for i in range(7):
    print(i)

for i in range(2,7):
    print(i)

for i in range(2,10,2):
    print('ff',i)

for i in range(8,2,-3):
    print(i)


student_marks = [30,45,75,56]
new_student_marks =[]
for mark in student_marks:
    new_student_marks.append(mark+5)
print(new_student_marks)




players_name =[]
for i in range(1,6):  
    name=input(f'player {i}:')
    players_name.append(name)
print(players_name)