#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.

Bill = float(input("What is the total bill?"))
Party = int(input("How many people are in your party?"))
Tip_int = int(input("What percentage would you like to tip?"))
Tip_float = Tip_int / 100
Total_bill = Bill * (1 + Tip_float)
Total_each = Total_bill / Party
Total_each = "{:.2f}".format(Total_each)
print(f"Each person should pay ${Total_each}")