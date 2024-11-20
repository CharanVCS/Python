def main():
    nutrition_info = {
        "apple": 130,
        "avocado": 50,
        "kiwifruit": 90,
        "pear": 100,
        "sweet cherries": 100,
        "banana": 105,
        "cantaloupe": 50,
        "grapefruit": 52,
        "grapes": 62,
        "honeydew melon": 61,
        "lemon": 17,
        "lime": 20,
        "nectarine": 62,
        "orange": 62,
        "peach": 59,
        "pineapple": 50,
        "plums": 30,
        "strawberries": 4,
        "tangerine": 47,
        "watermelon": 86
    }

    fruit = input("Item: ").strip().lower()

    if fruit in nutrition_info:
        print(f"Calories: {nutrition_info[fruit]}")
main()
