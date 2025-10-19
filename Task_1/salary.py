
def total_salary(path: str):

    try:
        with open(path,'r', encoding='utf-8') as file:
            employee_list = [s.strip().split(',') for s in file.readlines()]
            total_salary = sum(int(salary) for _, salary in employee_list)
            return (total_salary, total_salary / len(employee_list))
            
    except FileNotFoundError:
        return (0,0)


total, average = total_salary('Task_1/salary.txt')
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
