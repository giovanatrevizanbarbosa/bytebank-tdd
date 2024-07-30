from model.employee import Employee


giovana = Employee('Giovana Trevizan', '18/04/2005', 1000)
banana = Employee('Banana Workaholic', '22/02/2002', 200000)

print(f"Salário normal: {giovana._salary}\nBônus: {giovana.calculate_bonus()}")
print(f"Salário normal: {banana._salary}\nBônus: {banana.calculate_bonus()}")