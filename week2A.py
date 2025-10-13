#STEP-1 Inputs
student_name=input("enter your name:")
#Monthly income (scholarship + part-time job)
scholarship = float(input("Enter your scholarship income: "))
part_time = float(input("Enter your part-time job income: "))
monthly_income=scholarship+part_time
#Fixed expenses: Dorm/rent, meal plan, textbooks (monthly average)
dorm_rent=float(input("enter your rent price:"))
meal_plan=float(input("meal plan:"))
textbooks=float(input("textbooks (monthly average):"))
fixed_expenses=dorm_rent+meal_plan+textbooks
#Variable expenses: Personal items, social activities, transportation
personal_items=float(input("personal items:"))
social_activities=float(input("social activities:"))
transportation=float(input("transportation:"))
variable_expenses=personal_items+social_activities+transportation
#Current savings balance
savings_balance=float(input("saving balance:"))
#Emergency fund goal (recommended: 3 months of expenses)
month_expenses=(fixed_expenses+variable_expenses)
fund_goal=3*month_expenses
#Has student loan (yes/no)
has_loan = input("Do you have a student loan? (yes/no): ")
#STEP-2 Calculations
#Total monthly expenses
total_expenses_m=fixed_expenses+variable_expenses

#Monthly net savings (income - expenses)
net_savings_m=monthly_income-total_expenses_m

#Savings rate percentage
saving_percentage=(net_savings_m/monthly_income)*100

#Expense-to-income ratio (expenses / income)
income_ratio=total_expenses_m/monthly_income

#Three months of expenses (for emergency fund)
three_month_expenses = fund_goal

#Months needed to reach emergency fund (goal / monthly_savings)
months_needed=fund_goal/net_savings_m

#Emergency fund gap (goal - current_savings)
fund_gap=fund_goal-savings_balance


#Recommended minimum savings for loan holders (15% of income)
