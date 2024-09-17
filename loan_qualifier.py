#CS 175
#Christopher Kenny
#Loan Qualifier

#Setting Variables
salary = False
years_on_job = False

#Qualifications for loan
salary = int(input("Enter how much you make per year: "))

if salary >= 30000:
  years_on_job = int(input("How long were you employed for (In years)? "))
  if years_on_job >= 2:
    print("You qualify for the loan")
  else:
   print("You must have been employed for at least 2 years to qualify.")
else:
  print("You must make at least $30,000 per year to qualify.")
