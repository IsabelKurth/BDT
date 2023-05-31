import csv

input_file = 'clothing.csv'
output_file = 'clothing_updates.csv'

# Open the input file for reading and the output file for writing
with open(input_file, 'r', newline='') as infile, open(output_file, 'w', newline='') as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile, quoting=csv.QUOTE_ALL)

    # Iterate over each row in the input file
    for row in reader:
        processed_row = []

        # Iterate over each field in the row
        for field in row:
            # Check if the field contains an unquoted newline character
            if '\n' in field and not field.startswith('"') and not field.endswith('"'):
                # Add double quotation marks to the field to properly quote the newline
                field = f'"{field}"'

            processed_row.append(field)

        # Write the processed row to the output file
        writer.writerow(processed_row)

print('Pre-processing completed.')