def calculate_expenses(price, quantity):
    return price * quantity


# List of prices and quantities for each item
prices = [10.99, 5.99, 3.49, 7.99]
quantities = [2, 3, 5, 1]

# Calculate the expenses for each item
expenses = list(map(calculate_expenses, prices, quantities))

# Calculate the total expenses
total_expenses = sum(expenses)

# Print the results
print(f"Item Prices: {prices}")
print(f"Item Quantities: {quantities}")
print(f"Expenses for Each Item: {expenses}")
print(f"Total Expenses: {total_expenses}")
