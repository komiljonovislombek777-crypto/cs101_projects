student_name=input("enter your name:")

scholarship = float(input("Enter your scholarship income: $"))
part_time_job = float(input("Enter your part-time job income: $"))
monthly_income=scholarship+part_time_job

dorm_rent=float(input("enter your rent price:$"))
meal_plan=float(input("meal plan:$"))
textbooks=float(input("textbooks (monthly average):$"))
fixed_expenses=dorm_rent+meal_plan+textbooks

personal_items=float(input("personal items:$"))
social_activities=float(input("social activities:$"))
transportation=float(input("transportation:$"))
variable_expenses=personal_items+social_activities+transportation

current_savings_balance=float(input("Current saving balance:"))

total_monthly_expenses=(fixed_expenses+variable_expenses)

fund_goal=3*total_monthly_expenses
has_loan = input("Do you have a student loan? (yes/no): ")
student_loan = has_loan == 'yes'
monthly_net_savings = monthly_income-total_monthly_expenses

saving_rate_percentage = (monthly_net_savings/ monthly_income) * 100


income_ratio = total_monthly_expenses / monthly_income

three_month_expenses = fund_goal

months_needed_to_reach_emergency = fund_goal/monthly_net_savings

fund_gap=fund_goal-current_savings_balance

Critical = income_ratio > 0.95

Risky = income_ratio > 0.85 and income_ratio <= 0.95

Acceptable = income_ratio > 0.70 and income_ratio <= 0.85

Healthy = income_ratio <= 0.70

Emergency_fund_adequate = current_savings_balance >= fund_goal

Has_student_loan =  has_loan

Savings_below_recommended_for_loan_holder =  student_loan and current_savings_balance < 15

print("\n--- FINANCIAL HEALTH STATUS ---")
print(f"Critical: {Critical}")
print(f"Risky: {Risky}")
print(f"Acceptable: {Acceptable}")
print(f"Healthy: {Healthy}")
print(f"Emergency fund adequate: {Emergency_fund_adequate}")
print(f"Has student loan: {Has_student_loan}")
print(f"Savings below recommended for loan holder: {Savings_below_recommended_for_loan_holder}")

print("\n--- SUMMARY  ---")
print(f"Expense-to-Income Ratio: {income_ratio:.2f}")
print(f"Savings Rate: {saving_rate_percentage:.2f} %")
print(f"Emergency Fund Goal: {fund_goal:.2f}")
print(f"Current Savings: {current_savings_balance:.2f}")
print(f"Emergency Fund Gap: {fund_gap:.2f}")
print(f"Months Needed to Reach Goal: {months_needed_to_reach_emergency:.1f}")