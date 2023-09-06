def replace_terrible(input_file, output_file):
    with open(input_file, 'r') as file:
        text = file.read()

    # Count the occurrences of "terrible"
    count = text.count("terrible")

    # Replace even occurrences with "pathetic" and odd occurrences with "marvellous"
    replaced_text = text.replace("terrible", "pathetic", count % 2 == 0)
    replaced_text = replaced_text.replace("terrible", "marvellous")

    with open(output_file, 'w') as file:
        file.write(replaced_text)

    return count

input_file = "file_to_read.txt"
output_file = "result.txt"

count = replace_terrible(input_file, output_file)
print("Number of occurrences of 'terrible':", count)