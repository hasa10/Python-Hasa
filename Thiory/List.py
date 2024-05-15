marks=[23,67,78,50,67] #Ordered collection and mutable
print(marks)
print(type(marks))
print(marks[2])
print(len(marks))
marks[2]=99
print(marks[2])#99
#marks[7]=12    IndexError: list assignment index out of range
marks.append(4)
print(marks)  #[23, 67, 99, 50, 67, 4]
marks.append('HI')
print(marks)   # [23, 67, 99, 50, 67, 4, 'HI']
marks[0]='Hello'
print(marks) # ['Hello, 67, 99, 50, 67, 4, 'HI'] 

student=['cham','sona','chathu','Hasa']
print(student+marks)  # ['cham', 'sona', 'chathu', 'Hasa', 23, 'Hello', 99, 50, 67, 4, 'HI']
print(student.index('sona'))   # 1
print(marks.index(67))  # 1
print(marks.index(67,0,2)) # 1
print(marks.index(67,-3,))  # 4
print(marks.count(67))    # 2
print(marks.pop())   # HI
print(marks)    # ['Hello', 67, 99, 50, 67, 4]   anthima eka ain weno
marks.pop() # remove last number from List
print(marks)   # ['Hello', 67, 99, 50, 67]
marks.pop(1)
print(marks)   # ['Hello', 99, 50, 67]
marks.remove(99)
print(marks)    # ['Hello', 50, 67]
marks.extend([56,76])
print(marks)   # ['Hello', 50, 67, 56, 76]
marks.insert(2,46)
print(marks)   # ['Hello', 50, 46, 67, 56, 76]
marks2 = marks.copy()
print(marks2)
marks.reverse()
print(marks)   #  [76, 56, 67, 46, 50, 'Hello']
marks2.clear()
print(marks2)  # []
del(marks2)
print(marks2)