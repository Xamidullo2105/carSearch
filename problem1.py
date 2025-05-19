
def replacement(currencies:dict, currency:str, money:int):
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
input_money = int(input("Enter your money: "))
input_currency = input("Enter a currency: ")

result = replacement(exchange_rates, input_currency, input_money)
print(result)