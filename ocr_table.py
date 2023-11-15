import pytesseract
from PIL import Image
import csv
import re

# Define the source file
source_file = '/Users/guntar/Documents/KerjaanPJB/Data/tabel/142C_1_13.jpg'

# Use pytesseract to extract text from the image
image = Image.open(source_file)
text = pytesseract.image_to_string(image)

# Process the text
# Assuming the table data is separated by newlines and spaces/tabs
# Adjust the splitting logic according to the actual text output
lines = text.strip().split('\n')

# Prepare the data for CSV
table_data = []
for line in lines:
    # Split each line by multiple spaces or tabs that separate the columns
    # Adjust the regex pattern if needed to suit your table's format
    columns = re.split(r'\s{2,}|\t+', line.strip())
    table_data.append(columns)

# Define the CSV file path
csv_file_path = '/Users/guntar/Documents/KerjaanPJB/Data/tabel/142C_1_13.csv'

# Write to CSV
with open(csv_file_path, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(table_data)

print(f'Table data has been written to {csv_file_path}')
