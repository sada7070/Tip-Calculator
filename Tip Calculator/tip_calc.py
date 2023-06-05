print("Welcome to the tip calculator.")

Bill=input("What was the total bill? $")
bill=float(Bill)

Tip=input("What percentage tip would you like to give? 10, 12, or 15? ")
tip=int(Tip)

Split_no=input("How many people to split the bill? ")
split_no=int(Split_no)

tip_money=(bill*tip)/100

bill+=tip_money

ind_bill=bill/split_no

final_bill=round(ind_bill, 2)

print(f"Each person should pay: ${final_bill}")
