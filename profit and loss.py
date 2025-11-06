sell=int(input("Enter how much you sold the item for: "))
buy=int(input("Enter how much you bought the item for: "))

if sell>buy:
    profit=sell-buy
    print("You made a profit of ",profit)
else:
    loss=buy-sell
    print("You have a loss of ",loss)