#Functions

def get_input():
    length_of_journey = float(input("Please enter your length of journey in miles: "))
    miles_per_gallon = float(input("Please enter the miles per gallon of the vehicle: "))
    price_of_fuel = float(input("Please enter the current price of fuel(in pence): "))
    return length_of_journey, miles_per_gallon, price_of_fuel

def calculate_cost(length_of_journey, miles_per_gallon, price_of_fuel):
    total_cost = (length_of_journey/miles_per_gallon)*price_of_fuel
    return total_cost

def display_cost(total_cost):
    print("The cost of fuel for the  journey is £{0}".format(total_cost))

#main
def main():
    user_input = get_input()
    calculate = calculate_cost(length_of_journey, miles_per_gallon, price_of_fuel)
    display = display_cost(total_cost)
