# Aussie tax per-transaction

For business owners who want to calculate the income tax they should put aside for each transaction that comes in, with the context of the history of transactions.

### Problem

Calculating tax as a sole trader goes as follows:

- Earn heaps of money.
- Spend all of it.
- Realize you need to pay tax.
- Use coming year's income to cover the last tax bill.

This one-file Python script (`app/app.py`) simplifies that by letting you input each transaction and calculate the income tax before and after it. As you input transactions, the estimated tax to allot is printed out.

### Note:

- Tax calculations are using ATO's 22/23 rates (https://atotaxrates.info/individual-tax-rates-resident/ato-tax-rates-2023/).
- This is not financial advice, and the estimates are just estimates. Any use is on your own.
