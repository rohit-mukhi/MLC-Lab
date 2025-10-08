import pandas as pd

bill = pd.DataFrame({
    'Name': ['Ketchup', 'Onions', 'Deodorant', 'Flour', 'Cookies', 'Soda'],
    'Quantity': [1, 2, 1, 2, 4, 2],
    'Price': [20, 18, 150, 23, 40, 30]
}, index=[1, 2, 3, 4, 5, 6])

bill['Total'] = bill['Quantity'] * bill['Price']

print("*** The Bill ***")
print(bill, "\n")

max_revenue_product = bill.loc[bill['Total'].idxmax()]
print("The product with maximum revenue is: ")
print(max_revenue_product)
