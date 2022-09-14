
import json
import os

"""
@Author Jack Hales (https://jackhales.com)
This application is for inputting the next transaction, and
providing the user with the amount of tax they should alot,
and putting it into the history.
"""

def calculate_full_income_tax(history):
    pass

# A generic function which will cast a result, and
# if it fails or is False, will ask again. If true,
# will return the result as if it was a filter.
def ask_till_type(msg, cast):
    wanting = False
    while not wanting:
        result = input(msg)
        try:
            cast_result = cast(result)
            if cast_result == True:
                return result
            elif cast_result == False:
                pass # do nothing, ask again
            elif cast_result != False:
                return cast_result
        except:
            pass
        print("> Please try again!")

# Make sure history exists.
if not os.path.exists("history.json"):
    open("history.json", "w").write("[]")
history = json.load(open("history.json"))

# Ask user for information.
earning_base = ask_till_type("> How much did you earn (base before tax)?: ", float)
top_tax_type = ask_till_type("> Is there any top-tax? (GST/NO): ", lambda r: r.lower() in ["gst", "no"])
top_tax_type = top_tax_type.lower() # lower for normalization
print("> Great, thanks!")

# Now to calculate the total notional.
top_tax = 0
if top_tax_type == "gst":
    top_tax = earning_base * 0.1 # to be added for notional
elif top_tax_type == "no":
    top_tax = 0
else:
    print(f"> Top tax type of '{top_tax_type}' is unknown!")
    exit()

print(f"> The top tax amount was calculated to be '{top_tax}'")
