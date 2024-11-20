def main():
    cost = 50
    accepted_coins = [25, 10, 5]
    total_inserted = 0

    while total_inserted < cost:
        print(f"Amount Due: {cost - total_inserted}")
        coin = int(input("Insert coin: "))
        if coin in accepted_coins:
            total_inserted += coin
        else:
            print("Invalid coin. Please insert a valid coin.")

    change = total_inserted - cost
    print(f"Change Owed: {change}")

if __name__ == "__main__":
    main()
