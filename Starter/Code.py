#Tony K.
#18/11/2014
#Functions - Starter 



#calculate basic pay
def calculate_basic_pay(hours,pay):
    basic_pay = hours*pay
    return basic_pay

#calculate overtime pay
def calculate_overtime_pay(hours,pay):
    basic_pay = hour * pay
    overtime_pay = (hours-40)*(pay*1.5)
    total_pay_and_overtime = basic_pay + overtime_pay
    return total_pay_and_overtime
    
