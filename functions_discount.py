def calculate_total(price,quantity):
    return price*quantity
def calculate_discount(total):
    if total>=5000:
        return total*0.20
    elif total>=2000:
        return total*0.10
    else:
        return "no discount"
def total_price(discount):
    return total-discount

total=calculate_total(5000,3)
discount=calculate_discount(total)
total_amt=total_price(discount)
print("Total price is :",total)
print("discounted price is :",discount)
print("total price after discount is given as:",total_amt)