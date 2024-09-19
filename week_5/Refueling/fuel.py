import sys

def main():
    while True:
        try:
            frac = input("Fraction: ")
            percentage = convert(frac)
            result = gauge(percentage)
            print(result)
            sys.exit(0)
        except (ValueError, ZeroDivisionError):
            pass

def convert(fraction):
    try:
        x, y = fraction.split('/')
        x = int(x)
        y = int(y)
        if y == 0:
            raise ZeroDivisionError("Division by zero")
        if x > y:
            raise ValueError("Invalid fraction: numerator greater than denominator")
        return round((x / y) * 100)
    except (ValueError, ZeroDivisionError):
        raise

def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"

if __name__ == "__main__":
    main()
