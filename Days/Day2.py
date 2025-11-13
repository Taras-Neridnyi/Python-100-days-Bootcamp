print("tip calculator:")
total_bill = float(input("Enter the total bill: $"))
tip = float(input("Enter the tip amount: $"))
people = int(input("Enter the number of people: "))
bill_for_evr_person = (total_bill + tip) / people
print("The total bill for each person is $", bill_for_evr_person)

