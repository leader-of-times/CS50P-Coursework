amount_due = 50
print(f"Amount Due: {amount_due}")

while amount_due > 0:
    ins_coin = int(input("Insert Coin: "))
    if ins_coin in [5, 10, 25]:
        amount_due -= ins_coin
    else:
        print(f"Amount Due: {amount_due}")
        continue

    if amount_due > 0:
        print(f"Amount Due: {amount_due}")
    else:
        print(f"Change Owed: {abs(amount_due)}")
