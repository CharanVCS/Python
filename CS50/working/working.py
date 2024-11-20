import re
import sys

def main():
    try:
        print(convert(input("Hours: ")))
    except ValueError as e:
        sys.exit(e)

def convert(s):
    # Regular expression to match the two acceptable formats
    pattern = re.compile(r'^(\d{1,2})(?::(\d{2}))? (AM|PM) to (\d{1,2})(?::(\d{2}))? (AM|PM)$')
    match = pattern.match(s)
    if not match:
        raise ValueError("ValueError")

    start_hour, start_minute, start_period, end_hour, end_minute, end_period = match.groups()

    # Default minutes to "00" if they are not provided
    if start_minute is None:
        start_minute = "00"
    if end_minute is None:
        end_minute = "00"

    start_hour = int(start_hour)
    start_minute = int(start_minute)
    end_hour = int(end_hour)
    end_minute = int(end_minute)

    # Validate time ranges
    if not (1 <= start_hour <= 12 and 0 <= start_minute < 60):
        raise ValueError("ValueError")
    if not (1 <= end_hour <= 12 and 0 <= end_minute < 60):
        raise ValueError("ValueError")

    # Convert start time to 24-hour format
    if start_period == "PM" and start_hour != 12:
        start_hour += 12
    elif start_period == "AM" and start_hour == 12:
        start_hour = 0

    # Convert end time to 24-hour format
    if end_period == "PM" and end_hour != 12:
        end_hour += 12
    elif end_period == "AM" and end_hour == 12:
        end_hour = 0

    return f"{start_hour:02}:{start_minute:02} to {end_hour:02}:{end_minute:02}"

if __name__ == "__main__":
    main()

