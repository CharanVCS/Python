import random

def main():
    level = get_level()
    score = 0

    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        if solve_problem(x, y):
            score += 1

    print(f"Score: {score}")


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1, 2, 3]:
                return level
        except ValueError:
            pass
        print("Invalid level. Please enter 1, 2, or 3.")


def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)
    else:
        raise ValueError("Invalid level")


def solve_problem(x, y):
    attempts = 0
    correct_answer = x + y

    while attempts < 3:
        try:
            answer = int(input(f"{x} + {y} = "))
            if answer == correct_answer:
                return True
            else:
                print("EEE")
        except ValueError:
            print("EEE")

        attempts += 1

    print(f"{x} + {y} = {correct_answer}")
    return False


if __name__ == "__main__":
    main()
