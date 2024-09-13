def main():
    inp = input("File name: ").lower().strip()
    if inp.endswith(".gif"):
        print("image/gif")
    elif inp.endswith(".jpg") or inp.endswith(".jpeg"):
        print("image/jpeg")
    elif inp.endswith(".png"):
        print("image/png")
    elif inp.endswith(".pdf"):
        print("application/pdf")
    elif inp.endswith(".zip"):
        print("application/zip")
    elif inp.endswith(".txt"):
        print("text/"+ inp[:-4])
    else:
        print("application/octet-stream")

if __name__ == "__main__":
    main()
