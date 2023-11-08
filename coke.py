"""We are calculating how much money that the user owe, if they brought something."""
"""Sort of a coke machine."""
def coke_machine(amount_due):
    total_amount = 0
    coins = [25, 15, 5]
    while amount_due > 0:
        amount = print(f"Amount Due: {amount_due}. We only accept $25, $15 and $5")
        payment = int(input("Insert Coin: "))
        if payment in coins:
            amount_due -= payment
    return f"No amount due!"
    
def main():
    print(coke_machine(int(input("How much was it that you brought? "))))

if __name__ == "__main__":
    main()