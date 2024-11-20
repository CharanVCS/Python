def main():
    import sys
    from collections import defaultdict

    groceries = defaultdict(int)

    while True:
        try:
            item = input().strip().lower()
            if item:
                groceries[item] += 1
        except EOFError:
            break

    for item in sorted(groceries):
        print(f"{groceries[item]} {item.upper()}")
main()
