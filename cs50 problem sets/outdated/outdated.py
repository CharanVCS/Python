def main():
    import re
    months = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]

    month_to_number = {month: str(index + 1).zfill(2) for index, month in enumerate(months)}

    while True:
        date_str = input("Date: ").strip()

        # Try matching MM/DD/YYYY format
        if re.match(r'^\d{1,2}/\d{1,2}/\d{4}$', date_str):
            try:
                month, day, year = date_str.split('/')
                month = month.zfill(2)
                day = day.zfill(2)  
                year = int(year)
                if 1 <= int(month) <= 12 and 1 <= int(day) <= 31:
                    print(f"{year}-{month}-{day}")
                    break
            except ValueError:
                pass

        # Try matching "Month Day, Year" format
        elif re.match(r'^[A-Za-z]+ \d{1,2}, \d{4}$', date_str):
            try:
                month_str, day_year = date_str.split(' ', 1)
                day, year = day_year.split(', ')
                month = month_to_number[month_str]
                day = day.zfill(2)
                year = int(year)
                if 1 <= int(day) <= 31:
                    print(f"{year}-{month}-{day}")
                    break
            except (ValueError, KeyError):
                pass

if __name__ == "__main__":
    main()
