name= "Hasaranga"
print(len(name))
age=45
#print(len(age))      TypeError: object of type 'int' has no len()
age="45"
print(len(age))
print(type(age))
print(age.isdigit())
print(name.isdigit())
marks=90
#print(marks.isdigit())      AttributeError: 'int' object has no attribute 'isdigit'
marks='90'
print(marks.isdigit())
print(name.isalpha())
print(age.isalpha())
email='hasaranga@gmail.com'
print(email.isalpha())
temperature='-2'
print(temperature.isdigit())
password = 'hasa123'
print(password.isalnum())
print(email.isalnum())
print(temperature.isalnum())
print(age.isalnum())
print(name.isalnum())
name="hasaranga"
print(name.capitalize())   #mul akura capital karanu lebe.
print(name.casefold())  #siyaluma akuru simple karanu lebe.
print(name.swapcase())  #siyaluma akuru capital karanu lebe.
print(name.lower()) #hasaranga
name=name.capitalize()
print(name.swapcase())     #
