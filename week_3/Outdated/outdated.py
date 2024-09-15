def main():
    months = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]

    while True:
        try:
            date_input = input("Date: ").strip()

            if '/' in date_input:
                mm, dd, yyyy = map(int, date_input.split('/'))

            else:
                month_str, day_year_str = date_input.split(' ', 1)
                dd, yyyy = map(int, day_year_str.split(','))
                mm = months.index(month_str) + 1

            if 1 <= mm <= 12 and 1 <= dd <= 31 and yyyy > 0:
                print(f"{yyyy:04}-{mm:02}-{dd:02}")
                break
        except (ValueError, IndexError):
            continue

if __name__ == "__main__":
    main()
