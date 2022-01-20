#Welcome Message
print("Welcome to the tip calculator!")
# Asks user to enter the bill
bill=float(input("What was the total bill? $"))
# Asks user to enter the percentage of tip to be added to bill (tip should be written as integer excluding % sign)
tip=int(input("How much tip percentage would you like to give? "))
# converts tip entered to its percentsge format
tip_percent= tip * 0.01
# Asks user to enter the number of persons in order to split the bill amount
persons = int(input("How many people to split the bill? "))
# Calculates the amount each person has to pay along with tip
each_pay=(bill/persons) * (1+tip_percent)
# Rounds the amount to be paid by each person to 2 decimal places
each_pay_round = round(each_pay,2)
# for formatting the amount such that exactly 2 gits appear after decimal
each_pay_round_limit="{0:.2f}".format(each_pay_round)
# Displays the amount each person should pay
print(f"Each person should pay: ${each_pay_round_limit}")
