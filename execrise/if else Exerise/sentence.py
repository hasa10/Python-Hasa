'''sentence=input("Enter the sentences:")
#he_came_to_computer_lab. Then_he_went_to_home.After_that_he_had_dinner -------->I came to computer lab
sentence=sentence.replace("_"," ",)
sentence=sentence.replace("he","she")
print(sentence)'''


phone_number=input('Enter your phone number:')
#0717209990 -----> +94717209990


phone_number=phone_number.replace("0","+94",1)
print(phone_number)