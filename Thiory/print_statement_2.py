name='Hasaranga'
print('My Name is '+name)
print('My Name is',name)
name_2='Hasaranga'
print('My Name is',name,name_2)
print('My signature is',name+name_2)
print('My age is',20+7)
#print('My age is'+20+7)         TypeError: can only concatenate str (not "int") to str
age= 27
print('My Name is',name,'My age is',age)
print(f'My name is {name}.My age is {age}') # "f" akuru demiya uthuya ese nomethi uwoth siyaluma word print wei
print('My name is {}.My age is {}.'.format( name,age))
print(f'My name is {name}.\nMy age is{age}.\nMy second name is {name_2}')
print(name,'\n',age)
print("""My name is Hasaranga.
                  My name is 27""")
print(f'''My name is {name}.
                  My name is {age}''')
print(f'''My name is {name+name_2}.
                  My name is {age}''')
print(f"My name is {name}",end=' ')
print(name_2)



