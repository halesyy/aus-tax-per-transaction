
from app import calculate_full_income_tax
import json

"""
Sums the tax amounts in the `history.json` to print out
the total tax that should be held for the tax year.
"""

history = json.load(open("history.json"))
total_tax = calculate_full_income_tax(history)
total_income = sum([h["income"] for h in history])
print("> Total income (minus GST) for this period is: '{:.2f}'".format(total_income))
print("> The total tax from calculating the tax from history is '{:.2f}'".format(total_tax))
