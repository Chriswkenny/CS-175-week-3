#Christopher Kenny
#CS 175
import random
def lockerCombo():
  myName = input("Enter your name: ")
  num1 = random.randint(0,39)
  num2 = random.randint(0,39)
  num3 = random.randint(0,39)

#Checking Validity of Locker Combination
  if num1 != num2 and num2 != num3:
    print(f"{myName}'s locker combination is {num1}-{num2}-{num3}.")
    print("This combination will work.")
    return None
  else:
     print("Please try again, this is not a valid combination.")

#Output
lockerCombo()
