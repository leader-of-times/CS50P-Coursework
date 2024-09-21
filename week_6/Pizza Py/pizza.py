import sys
import csv
from tabulate import tabulate

def print_table(file_path):
    try:
        with open(file_path, 'r') as file:
            data = [row for row in csv.reader(file)]
            print(tabulate(data, headers='firstrow', tablefmt='grid'))

    except FileNotFoundError:
        sys.exit("File does not exist")

    except Exception as e:
        sys.exit(f"Error occurred while reading the file: {e}")

def main():
    if len(sys.argv) <= 1:
        sys.exit("Too few command-line arguments")

    elif len(sys.argv) >= 3:
        sys.exit("Too many command-line arguments")

    file_path = sys.argv[1]

    if not file_path.endswith(".csv"):
        sys.exit("Not a CSV file")

    print_table(file_path)

if __name__ == "__main__":
    main()
