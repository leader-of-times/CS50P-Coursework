def main():
    s = input("Input: ")
    short=shorten(s)
    print(short)

def shorten(s):
        ns = ""
        l = len(s)
        for i in range(l):
            if s[i] not in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
                ns += s[i]
        return ns


if __name__ == "__main__":
    main()
