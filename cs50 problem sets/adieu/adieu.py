def main():
    import sys

    names = []
    while True:
        try:
            name = input("Name: ")
            names.append(name)
        except EOFError:
            break

    if len(names) == 0:
        sys.exit("Error: No names were entered.")

    farewell_message = format_farewell(names)
    print(farewell_message)


def format_farewell(names):
    if len(names) == 1:
        return f"Adieu, adieu, to {names[0]}"
    elif len(names) == 2:
        return f"Adieu, adieu, to {names[0]} and {names[1]}"
    else:
        formatted_names = ", ".join(names[:-1]) + f", and {names[-1]}"
        return f"Adieu, adieu, to {formatted_names}"


if __name__ == "__main__":
    main()
