def main():
    a = input("What time is it? ")
    converted_time = convert(a)
    if 7.00 <= converted_time <= 8.00:
        print("breakfast time")
    elif 12.00 <= converted_time <= 16.00:
        print("lunch time")
    elif 18.00 <= converted_time <= 24.00:
        print("dinner time")
    else:
        print()

def convert(time):
    hours, minutes = time.split(":")
    hours = float(hours)
    minutes = float(minutes) / 60
    return hours + minutes

if __name__ == "__main__":
    main()
