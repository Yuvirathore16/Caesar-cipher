print("Welcome to tip calculator")
bill = float(input("What is the total bill? $"))
tip = int(input("how much tip would you like to give? 10, 12, 15?"))
people = int(input("how many people you would like to split?"))
bill_with_tip = tip/100 * bill + bill 
payment = bill_with_tip / people
print(round(payment,2))