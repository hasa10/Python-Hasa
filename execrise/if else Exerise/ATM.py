print("welcome to Boc bank")
name=input("what's you name:")
input("Enter your account number:")
pin=input("Enter pin number:")
if len(pin)==4 and pin.isdigit() :
          Acc_Balance=float(input("Enter your Account Balance:"))
          while (True):
              transaction=input("Do you want to withdraw or deposit:").lower()
            #Enter the amount you want to deposit / Enter the

              if transaction=="withdraw":
                        withdraw=float(input("enter the amount you want to withdraw :"))
                        if Acc_Balance>withdraw:
                            Acc_Balance1=Acc_Balance-withdraw
                            print(f'mr.{name} your Account balance is:{ Acc_Balance}')

                        else:
                            print("sorry try again")
              elif transaction=="deposit":
                    deposit=float(input("enter the amount you want to deposit:"))
                    Acc_Balance=Acc_Balance+deposit
                    print(f'mr.{name} your Account balance is:{ Acc_Balance}')

              else:
                    print("error")
              again = input("Do you want todo another transaction:").upper()
              if again == 'YES':
                  continue
              elif again == 'NO':
                  print('Thank you')
                  break
              else:
                  print('Invalid answer')


          else:
            print("try again")

