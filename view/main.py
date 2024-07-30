from model.employee import Employee

giovana = Employee('Giovana Trevizan', '18/04/2005', 1000)

print(f"Salário normal: {giovana._salary}\nBônus: {giovana.calculate_salary_bonus()}")