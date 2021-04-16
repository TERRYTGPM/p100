class ATM(object):
     def __init__(self, cardnumber, pin, bal):
          self.cardnumber = cardnumber
          self.pin = pin
          self.bal = bal


     def checkBal(self):
          print(self.bal)
     
     def withdrawMoney(self, money):
          newbal = self.bal - money
          print("Your new balance is " + str(newbal))
        
def main():
     cardnumber = input("Insert your card number: ")
     pin = input("Insert your pin number: ")
     Adwit = ATM(cardnumber, pin, 10000000000000000)
     print("choose what you wish to do: ")
     print("1. balance inquiry")
     print("2. Withdrawl")

     activity = int(input("Enter thy option: "))

     if activity == 1:
         Adwit.checkBal()
     elif activity == 2:
         amount = int(input("How much do you wish to withdraw? "))
         Adwit.withdrawMoney(amount)
     else:
          print("what do I look like, a dumbass? enter a valid option")

main()

