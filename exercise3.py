student_name=input("what is your name:")
gpa = float(input("Enter GPA (0.0-4.0): "))
total_credit_hours=int(input("enter hours:"))
Dean_list_requirements = total_credit_hours >= 12 and gpa >= 3.5
print(f"name:{student_name}")
print(f"gpa:{gpa}")
print(f"requirements:{total_credit_hours}")
print(f"student`s status:{"yes"if Dean_list_requirements else "no"}")
