def convert(a):
    a = a.replace(":)", "🙂")
    a = a.replace(":(", "🙁")
    return a

def main():
    user = input()
    fs= convert(user)
    print(fs)

if __name__ == "__main__":
    main()
