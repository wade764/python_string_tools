import sys

def reverse_lines(input_file, output_file):
    try:
        with open(input_file, 'r') as file:
            lines = file.readlines()

        reversed_lines = [line.strip()[::-1] + '\n' for line in lines]

        with open(output_file, 'w') as file:
            file.writelines(reversed_lines)

        print(f"Output successfully written to {output_file}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py input.txt output.txt")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    reverse_lines(input_file, output_file)

