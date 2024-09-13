def main():
    choice=input("What is the Answer to the Great Question of Life, the Universe and Everything? ").strip()
    match choice.lower():
        case "42":
            print("Yes")
        case "forty-two":
            print("Yes")
        case "forty two":
            print("Yes")
        case _:
            print("No")

main()
