def main():
    while(True):
        try:
            frac=input("Fraction: ")
            x, y = frac.split('/')
            x = int(x)
            y = int(y)
            if y == 0 or x > y:
                continue

            percentage=(x/y)*100

            if percentage <=1:
                    print("E")
            elif percentage>=99:
                    print("F")
            else:
                    print(round(percentage),end='%')
            break
        except(ValueError,ZeroDivisionError):
                continue


main()


