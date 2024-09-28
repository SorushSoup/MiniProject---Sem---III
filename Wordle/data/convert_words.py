# Function to read words from 'words.txt', separate them, and save to 'wordle_words.txt'
def separate_words_from_file(input_file, output_file):
    try:
        # Open the input file and read the line
        with open(input_file, 'r') as infile:
            line = infile.readline().strip()  # Read the first line and remove any extra whitespace
        
        # Split the line into words
        words = line.split()
        
        # Open the output file and write each word on a new line
        with open(output_file, 'w') as outfile:
            for word in words:
                outfile.write(word + '\n')  # Write each word followed by a newline
        
        print(f"Words have been separated and saved to '{output_file}'.")

    except FileNotFoundError:
        print(f"Error: The file '{input_file}' does not exist.")

# Specify the input and output files
input_file = 'data/words.txt'
output_file = 'data/wordle_words.txt'

# Call the function
separate_words_from_file(input_file, output_file)
