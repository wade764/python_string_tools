import sys

def reverse_content_and_order(input_file, output_file):
    try:
        with open(input_file, 'r') as file:
            lines = file.readlines()

        # Reverse the content of each line
        reversed_lines_content = [line.strip()[::-1] for line in lines]

        # Reverse the order of lines
        reversed_lines_order = reversed_lines_content[::-1]

        # Combine the content with line breaks
        final_content = '\n'.join(reversed_lines_order) + '\n'

        with open(output_file, 'w') as file:
            file.write(final_content)

        print(f"Output successfully written to {output_file}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py input.txt output.txt")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    reverse_content_and_order(input_file, output_file)

