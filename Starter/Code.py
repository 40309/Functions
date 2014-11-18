#Tony K.
#18/11/2014
#Functions - Starter 



#calculate basic pay
def calculate_basic_pay(hours,pay):
    basic_pay = hours*pay
    return basic_pay

#calculate overtime pay
def calculate_overtime_pay(hours,pay):
    basic_pay = 40 * pay
    overtime_pay = (hours - 40)*(pay * 1.5)
    total_pay_and_overtime = basic_pay + overtime_pay
    return total_pay_and_overtime

#def calculate total pay
def calculate_toal_pay(hours,pay):
    if hours <=0:
        total_pay = calculate_basic_pay(hours,pay)
    else:
        calculate_overtime_pay(hours,pay)
    return total_pay

#Get Work details
def work_details():
    hours = int(input("Please enter the amount of hours you have worked: "))
    pay = float(input("Please enter your pay rate: "))
    return hours,pay

#Display Pay
def display_total_pay(total):
    print("You have earned £{0} is month".format(total))
