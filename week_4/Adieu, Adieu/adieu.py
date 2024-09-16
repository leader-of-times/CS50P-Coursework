import sys
import inflect

def main():
    p=inflect.engine()
    names=[]

    try:
        while True:
            print("Name: ",end="")
            name=input().strip()
            if name:
                names.append(name)
    except EOFError:
        pass

    if names:
        formatted_names=p.join(names)
        print(f"Adieu, adieu, to {formatted_names}")

if __name__ == "__main__":
    main()
