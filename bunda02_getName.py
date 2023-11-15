import os
from pdf2image import convert_from_path
import pytesseract
import re


def extract_name(text):
    # First pattern
    pattern = r'Nama \(Name\) :\s*\[?([^\]\n]+)\]?\s*Nomor NIK/Paspor'
    match = re.search(pattern, text, re.IGNORECASE)
    if match:
        return match.group(1).strip()

    # Second pattern
    pattern = r': (.*?)(?=\n\n: \d{10,20})'
    match = re.search(pattern, text)
    if match:
        return match.group(1).strip()

    # Third pattern
    pattern = r'Nama \(Name\) [>: -]+(.*)'
    match = re.search(pattern, text)
    if match:
        return match.group(1).strip()
    
    # Fourth pattern
    pattern = r'\n[>-]\s*([A-Za-z\s]+)'
    match = re.search(pattern, text)
    if match:
        return match.group(1).strip()

    return None


# Set the source folder and the output file
# source_folder = 'E:\\OneDrive\Documents\\WorkingFiles\\PENDING DJK 2021\\PENDING - 0921 Sertifikasi DJK\\Batch 1_UBJOM PULPIS\\'
source_folder = r'E:\DataKerja\PENDING DJK 2021\PENDING - 0921 Sertifikasi DJK\Batch 3\\'
output_file_path = os.path.join(source_folder, 'extraction_results.txt')
failed_content_path = os.path.join(source_folder, 'failed_content.txt')

# Page where the data is located
data_location = 1  # Set to 2 as default, change this as needed

# Initialize counters
total_files = 0
successful_extractions = 0
failed_extractions = 0

# Open (or create) the output file and overwrite if it already exists
with open(output_file_path, 'w') as output_file, open(failed_content_path, 'w') as failed_content_file:
    # Write the source folder path at the beginning of the output file
    output_file.write(f"Source folder: {source_folder}\n\n")

    # Process each PDF file in the source_folder
    for filename in os.listdir(source_folder):
        if filename.lower().endswith('.pdf'):
            total_files += 1
            pdf_path = os.path.join(source_folder, filename)
            print(f'🔸 Processing file: {filename}')  # Only print the file name

            # Convert the specific page of the PDF into an image
            try:
                pages = convert_from_path(
                    pdf_path, first_page=data_location, last_page=data_location, dpi=500)
                text = pytesseract.image_to_string(pages[0]) if pages else ''

                # Extract name
                name = extract_name(text)
                if name:
                    print(f"Extracted name: '{name}'")
                    output_file.write(f"{name}\n")
                    successful_extractions += 1
                else:
                    print(f"Name could not be extracted from {filename}")
                    output_file.write(f"<FAILED> on {filename}\n")
                    # Write the failed text content
                    failed_content_file.write(text + "\n\n\n")
                    failed_extractions += 1
            except Exception as e:
                print(f"An error occurred while processing {filename}: {e}")
                output_file.write(f"<FAILED> on: {filename}\n")
                failed_content_file.write(
                    f"Error processing {filename}: {e}\n\n\n")  # Write error message
                failed_extractions += 1

    # Write the recap at the end of the output file
    recap = f"\nTotal files read: {total_files}\nSuccessful extractions: {successful_extractions}\nFailed extractions: {failed_extractions}\n"
    output_file.write(recap)

print('\n✨ Finished OCR processing and name extraction for all PDF files.')
