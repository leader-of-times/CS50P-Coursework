def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * (percent/100)
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    slice=d.lstrip("$")
    dollar=float(slice)
    return dollar


def percent_to_float(p):
    slice=p.rstrip("%")
    percents=float(slice)
    return percents


main()
