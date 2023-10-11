import math
#display the first output that the user will see using print fun. Request user input on choice of repayment
print("Investment - to calculate the amount of intrest you'll earn on your investment.")
print("Bond - to calculate the amount you'll have to pay on a home loan.")
repayment_choice = input("Enter either 'investment' or 'bond' from the menu above to proceed: ").lower()
#I was confused on how to allow user input to capitalize 
# so i researched and found help on this link https://stackoverflow.com/questions/12719586/how-to-let-python-recognize-both-lower-and-uppercase-input
if repayment_choice == "bond":
    print("You have choosen " + repayment_choice + " as your repayment choice.")
    p = float(input("Enter the value of the house(e.g.100000): "))
    i = float(input("Enter the interest rate(e.g.7): "))/100
    n = float(input("Enter the number of months you plan to repay the bond(e.g.120): "))
    repayment = (i * p)/ (1- (1 + i)** (-n)) 
#I used th math function to round of my calculations
    monthly_repayment = math.floor(repayment/12)
    print("Your monthly repayment is: R" + str(monthly_repayment))
elif repayment_choice == "investment":
    print("You have choosen " + repayment_choice + " as your repayment choice.")
    p = float(input("Enter the amount of money you are depositing: "))
    r = float(input("Enter the intrest rate (NB.numbers only!):"))/100
    t = float(input("Enter the number of years you plan on investing: "))
    interest = input("Choose interest type: 'simple' or 'compound'. ")
#I intented another if and elif statement in order to allow the user to choose a interest type.
    if interest == "simple":
        simple = p * (1 + r*t)
        simple_interest = math.floor(simple)
        print("Your investment amount will be R" + str(simple_interest) + " on simple interest.")

    elif interest == "compound":
        compound = p * math.pow((1+r),t)
        compound_interest = math.floor(compound)
        print("Your investment amount will be R" + str(compound_interest) + " on compound interest.")
        
else:
    print("Your input is incorrect. Please try again! ")


    


