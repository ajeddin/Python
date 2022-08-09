stock_prices= [('APPL', 200),("GOOG", 300),("ASC",1000)]
for item in stock_prices:
    print(item)

for ticker,price in stock_prices:
    print(ticker)
work_hours = [("Abby", 100), ("Mark", 85), ("Jesse", 103), ("Husam", 213)]
def employee_check(work_hours):
    current_max = 0
    employee_month = ''
    for employee,hours in work_hours:
        if hours > current_max:
            current_max=hours
            employee_month=employee
        else:
            pass
    return (employee_month,current_max)
print(employee_check(work_hours))
name,hours= employee_check(work_hours)
print(name)
print(hours)