def main():
    x,y,z=input("Expression: ").split(" ")
    x=float(x)
    z=float(z)
    if(y=='+'):
        print(float(x+z))
    elif(y=='-'):
        print(float(x-z))
    elif(y=='*'):
        print(float(x*z))
    elif(y=='/'):
        print(float(x/z))
    else:
        print()

if __name__ == "__main__":
    main()
