



#calculate basic pay
def calculate_basic_pay(hours,pay):
    basic_pay = hours*pay
    return basic_pay

#calculate overtime pay
def calculate_overtime_pay(hours,pay):
    overtime_pay = (hours-40)*(pay*1.5)
    return overtime_pay


    
