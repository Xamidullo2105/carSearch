def purchase_calculation(cart, prices):
    total_purchase = 0
    for product, amount in cart.items():
        total_purchase += amount * prices[product]
    return total_purchase

cart = {
    "Olma": 3,
    "Banan": 2,
    "Uzum": 5,
}
prices = {
    "Olma": 1200,
    "Banan": 1800,
    "Uzum": 1500,
}

result = purchase_calculation(cart, prices)
print(f"Total purchase --> {result} ming so'm")
