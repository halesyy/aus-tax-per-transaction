
import json

"""
Sums the tax amounts in the `history.json` to print out
the total tax that should be held for the tax year.
"""

history = json.load(open("history.json"))
total = sum([h["tax"] for h in history])
print("> Total tax that should be held for this period is: '{:.2f}'".format(total))
