basic=float(input("Enter basic salary: "))
hra_percent=float(input("Enter HRA (%): "))
ma_percent=float(input("Enter medical allowance (%): "))
tax_percent=float(input("Enter tax (%): "))
bonus_percent=float(input("Enter bonus (%): "))

hra=basic*hra_percent/100
ma=basic*ma_percent/100
tax=basic*tax_percent/100
bonus=basic*bonus_percent/100

gross=basic+hra+ma+bonus
net_salary=gross-tax

print("\n========= Salary Breakdown ===========")
print("Basic salary: ",basic)
print("HRA: ",hra)
print("Medical allowance: ",ma)
print("Bonus: ",bonus)
print("Tax: ",tax)
print("---------------------------------------")
print("Gross salary: ",gross)
print("Net salary: ",net_salary)
print("---------------------------------------")