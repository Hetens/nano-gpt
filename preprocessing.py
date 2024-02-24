import re

def remove_datetime(text):
    # Define the pattern for matching date time
    pattern = r'\d{1,2}/\d{1,2}/\d{2}, \d{1,2}:\d{1,2}\s?[AP]M - '

    # Use regular expression to remove date time
    return re.sub(pattern, '', text)

def main():
    # Input and output file paths
    input_file = 'soha.txt'
    output_file = 'output.txt'

    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            data = f.readlines()

        # Remove date time from each line
        modified_data = [remove_datetime(line) for line in data]

        # Write modified data to output file
        with open(output_file, 'w', encoding='utf-8') as f:
            f.writelines(modified_data)

        print("Date time removed successfully. Output written to", output_file)

    except FileNotFoundError:
        print("Input file not found.")

if __name__ == "__main__":
    main()
