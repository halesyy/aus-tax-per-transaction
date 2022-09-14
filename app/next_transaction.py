
import json
import os

"""
@Author Jack Hales (https://jackhales.com)
This application is for inputting the next transaction, and
providing the user with the amount of tax they should alot,
and putting it into the history.
"""

def calculate_full_income_tax(history):
    income = sum([h["income"] for h in history])
    if income <= 18200:
        tax = 0
    elif income <= 45000:
        tax = (income - 18200) * 0.19
    elif income <= 120000:
        tax = (income - 45000) * 0.325 + 5092
    elif income <= 180000:
        tax = (income - 120000) * 0.37 + 29467
    else:
        tax = (income - 180000) * 0.45 + 51667
    return tax

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

while True:

    # Ask user for information.
    earning_base = ask_till_type("> Transaction income (base before tax)?: ", float)
    top_tax_type = ask_till_type("> Is there any top-tax? (GST/NO/INCGST): ", lambda r: r.lower() in ["gst", "no", "incgst"])
    top_tax_type = top_tax_type.lower() # lower for normalization
    print("> Great, thanks!")

    # Now to calculate the top tax piece amount.
    top_tax = 0
    if top_tax_type == "gst":
        top_tax = earning_base * 0.1 # to be added for notional
    elif top_tax_type == "no":
        top_tax = 0
    elif top_tax_type == "incgst":
        top_tax = earning_base / 11
        earning_base = earning_base / 11 * 10
    else:
        print(f"> Top tax type of '{top_tax_type}' is unknown!")
        exit()

    print(f"> The income component amount was calculated to be '{earning_base}'")
    print(f"> The top tax (GST/etc) amount was calculated to be '{top_tax}'")

    # Calculate the notional.
    notional = earning_base + top_tax

    input("> Click enter to add this to the history...")

    total_tax_before = calculate_full_income_tax(history)

    # Add to history.
    history.append({
        "income": earning_base, # income
        "tax": top_tax,
        "total": notional
    })

    total_tax_after = calculate_full_income_tax(history)
    tax_delta = total_tax_after - total_tax_before

    # Print out what everyone wants to know!
    print(f"> The tax you should allot for this transaction is: '{tax_delta}'")

    # Save.
    print("> Saving...")
    open("history.json", "w").write(json.dumps(history, indent=4))
    print("----------------------------")
