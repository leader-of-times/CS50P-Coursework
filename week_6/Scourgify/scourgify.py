import sys
import csv

def main():
    if len(sys.argv) != 3:
        sys.exit("Usage: python scourgify.py input.csv output.csv")

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    try:
        with open(input_file, newline='') as file_1:
            reader = csv.DictReader(file_1)

            # Prepare to write to the output CSV file
            with open(output_file, mode='w', newline='') as file_2:
                fieldnames = ['first', 'last', 'house']
                writer = csv.DictWriter(file_2, fieldnames=fieldnames)
                writer.writeheader()

                for row in reader:
                    last, first = row['name'].split(', ')
                    writer.writerow({'first': first, 'last': last, 'house': row['house']})
    except FileNotFoundError:
        sys.exit(f"Could not read {input_file}")

if __name__ == "__main__":
    main()
