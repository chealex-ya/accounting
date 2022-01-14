from people import get_employees
from salary import calculate_salary
from datetime import date

if __name__ == '__main__':
    print('Hi, accountant')
    get_employees(10)
    calculate_salary('Alex')
    print(date.today())


