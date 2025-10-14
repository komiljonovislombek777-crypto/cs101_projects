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
savings_balance=float(input("Current saving balance:"))
#Emergency fund goal (recommended: 3 months of expenses)
total_month_expenses=(fixed_expenses+variable_expenses)
fund_goal=3*total_month_expenses
#Has student loan (yes/no)
has_loan = input("Do you have a student loan? (yes/no): ")
if has_loan == "yes":
    print("You have a student loan.")
else:
    print("Perfect, you have no loan!")

#STEP-2 Calculations


#Monthly net savings (income - expenses)
net_savings_m=monthly_income-total_month_expenses

#Savings rate percentage
saving_percentage=(net_savings_m/monthly_income)*100

#Expense-to-income ratio (expenses / income)

income_ratio=total_month_expenses/monthly_income

#Three months of expenses (for emergency fund)
three_month_expenses = fund_goal

#Months needed to reach emergency fund (goal / monthly_savings)
months_needed=fund_goal/net_savings_m

#Emergency fund gap (goal - current_savings)
fund_gap=fund_goal-savings_balance


#Recommended minimum savings for loan holders (15% of income)
recommended_min_savings = 0.15 * monthly_income
critical = income_ratio > 0.95
risky = 0.85 < income_ratio <= 0.95
acceptable = 0.70 < income_ratio <= 0.85
healthy = income_ratio <= 0.70
emergency_fund_adequate = savings_balance >= fund_goal
has_student_loan = has_loan == "yes"
below_recommended = has_student_loan and saving_percentage < 15
print("\n--- FINANCIAL HEALTH STATUS ---")
print(f"Critical: {critical}")
print(f"Risky: {risky}")
print(f"Acceptable: {acceptable}")
print(f"Healthy: {healthy}")
print(f"Emergency fund adequate: {emergency_fund_adequate}")
print(f"Has student loan: {has_student_loan}")
print(f"Savings below recommended for loan holder: {below_recommended}")

# Optional summary
print("\n--- SUMMARY METRICS ---")
print(f"Expense-to-Income Ratio: {income_ratio:.2f}")
print(f"Savings Rate: {savings_rate:.2f}%")
print(f"Emergency Fund Goal: {fund_goal:.2f}")
print(f"Current Savings: {savings_balance:.2f}")
print(f"Emergency Fund Gap: {fund_gap:.2f}")
print(f"Months Needed to Reach Goal: {months_needed:.1f}")