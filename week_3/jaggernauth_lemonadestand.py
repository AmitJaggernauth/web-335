#Author: Amit Jaggernauth
#Date:1/31/2026
#File Name: jaggernauth_lemonadestand.py
#A simple program that calculates the cost and profit from running a lemonade stand.

# Function to calculate total cost of making lemonade

def calculate_cost(lemons_cost, sugar_cost):
    return lemons_cost + sugar_cost

# Function to calculate profit selling lemonade

def calculate_profit(lemons_cost, sugar_cost, selling_price):
        total_cost = lemons_cost + sugar_cost
        return selling_price - total_cost

# Test Variables

lemons_cost = 3.50
sugar_cost = 2.00
selling_price = 10.00

# Build output strings

cost_output = str(lemons_cost) + " + " + str(sugar_cost)  + " = " + str(calculate_cost(lemons_cost, sugar_cost))
profit_output = "Profit: " + str(calculate_profit(lemons_cost, sugar_cost, selling_price))

#Print results

print(cost_output)
print(profit_output)
