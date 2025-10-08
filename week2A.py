student_name=input("what is your name:")
monthly_income=float(input("enter (scholarship + part-time job:$"))
fixed_expenses=float(input("enter fixed expenses:$"))
variable_expenses=float(input("enter Variable expenses:$"))
current_balance=float(input("enter your Current savings balance:$"))
emergency_goal=float(input("Emergency fund goal:$"))
loan=input("do you have a student loan('yes' or 'no' ):")
total_monthly_expenses= fixed_expenses+variable_expenses
net_savings= monthly_income-total_monthly_expenses
saving_rate= net_savings/(total_monthly_expenses)*100
income_ratio=total_monthly_expenses/monthly_income




print(f"total monthly expenses:{total_monthly_expenses}")
print(f"monthly net savings:{net_savings}")
print(f"Savings rate percentage:{saving_rate}")
print(f"Expense-to-income ratio:{income_ratio}")



