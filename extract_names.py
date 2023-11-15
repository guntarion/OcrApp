import os
from PIL import Image
import pytesseract
import re
import shutil

# Function to extract the name and birthdate


def extract_details(text):
    name_match = re.search(r'Nama\s+:\s+([A-Z\s]+?)(?=\n|Name)', text)
    birthdate_match = re.search(
        r'Tempat,\s+tanggal\s+lahir\s+:\s+[A-Z\s]+,\s+(\d{2}-\d{2}-\d{4})', text)

    name = name_match.group(1).strip() if name_match else None
    birthdate = birthdate_match.group(1).strip() if birthdate_match else None

    return name, birthdate


# Set the starting number for file naming
starting_number = 1  # Change this to set the starting number manually

# Directories
source_dir = '/Users/guntar/Documents/KerjaanPJB/Data/bahankerja'
destination_dir = '/Users/guntar/Documents/KerjaanPJB/Data/bahansudah'

# Create destination directory if it doesn't exist
if not os.path.exists(destination_dir):
    os.makedirs(destination_dir)

# Process each .jpg file
for filename in os.listdir(source_dir):
    if filename.endswith('.jpg'):
        file_path = os.path.join(source_dir, filename)
        print(f'Processing file: {file_path}')

        # Perform OCR
        text = pytesseract.image_to_string(Image.open(file_path))
        name, birthdate = extract_details(text)

        if name and birthdate:
            # Create the new filename including the birthdate
            new_filename = f'2023-K3-{starting_number:03d} {name} {birthdate}.jpg'
            destination_path = os.path.join(destination_dir, new_filename)

            # Copy and rename the file to the new directory
            shutil.copy2(file_path, destination_path)
            print(f'File renamed and copied: {destination_path}')

            # Increment the file number
            starting_number += 1

            # Delete the original file
            os.remove(file_path)
            print(f'Original file deleted: {file_path}')
        else:
            print('Details could not be extracted.')

print('All files have been processed.')
