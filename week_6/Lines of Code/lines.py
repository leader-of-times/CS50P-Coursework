import sys
def count_lines(file_path):
    try:
        with open(file_path, "r") as file:
            count = 0
            inside_docstring = False

            for line in file:
                line = line.strip()

                # Skip blank lines
                if not line:
                    continue

                # Skip comments and lines inside docstrings
                if line.startswith("#") or inside_docstring:
                    continue

                # Handle docstrings
                if line.startswith('"""') or line.startswith("'''"):
                    if line.endswith('"""') or line.endswith("'''"):
                        continue  # Single-line docstring
                    inside_docstring = True
                    continue
                elif line.endswith('"""') or line.endswith("'''"):
                    inside_docstring = False
                    continue

                # Count valid line
                count += 1

            return count

    except FileNotFoundError:
        sys.exit("File does not exist")

    except:
        sys.exit("Error occurred while reading the file")

def main():
    if len(sys.argv) != 2:
        sys.exit("Incorrect number of command-line arguments")

    file_path = sys.argv[1]

    if not file_path.endswith(".py"):
        sys.exit("Not a Python file")

    num_lines = count_lines(file_path)
    print(num_lines)

if __name__ == "__main__":
    main()
