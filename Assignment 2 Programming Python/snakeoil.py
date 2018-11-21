# Assignment 2, Task 4
# Name: Naran Kongpithaksilp (Tan)
# Collaborators: None
# Time Spent: 00:06 hours (6:02 minutes)

def price(vol):
    totalPrice = 17 * vol
    if vol < 10:
        return float(totalPrice + 20*vol)
    elif vol >=10 and vol <= 100:
        return float(totalPrice + 500)
    elif vol > 100:
        return float(totalPrice * 0.97)

