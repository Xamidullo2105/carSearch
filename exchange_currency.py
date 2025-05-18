def exchange_currency(currencies: dict, currency: str, money: int):
    currency = currency.upper()
    if currency not in currencies:
        return "Invalid currency code"
    
    
    calculate_money = money / currencies[currency]
    return calculate_money

exchange_rates = {
        "USD": 12500,
        "EUR": 13500,
        "RUB": 150,
    }
    
inp_money = int(input("Enter your money: "))
inp_currency = input("Enter your currency: ")

result = exchange_currency(exchange_rates, inp_currency, inp_money)
print(result)