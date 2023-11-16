import os
import csv
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
    pattern = r'\n[>:-]\s*([A-Za-z\s]+)'
    match = re.search(pattern, text)
    if match:
        return match.group(1).strip()

    return None

def extract_qualification_code(text):
    pattern = r'KUALIFIKASI\.(\d)\.KIT[A-Z]+'
    match = re.search(pattern, text)
    return match.group(1).strip() if match else None

def extract_competency_unit(text):
    pattern = r'Unit Kompetensi \(Unit Competency\) : (.*)'
    matches = re.findall(pattern, text)
    return matches if matches else None

# Read the source folder from bunda00_daftarFolder.txt
with open('E:/Dropbox/0GPython/04ocrFiles/OcrApp/bunda00_daftarFolder.txt', 'r') as file:
    source_folders = file.read().splitlines()

# Define the output paths
csv_output_path = 'E:/JAPOGdrive/My Drive/01 PT JTB Projects/001 Sertifikat PJCA/csv_result.csv'
csv_competency_unit_path = 'E:/JAPOGdrive/My Drive/01 PT JTB Projects/001 Sertifikat PJCA/csv_comp_unit.csv'

# Process each source folder
for source_folder in source_folders:
    # Print a line break and the source folder
    print(f'\n🛢️ Processing folder: {source_folder}')
    # Set the output file
    output_file_path = os.path.join(source_folder, 'extraction_results.txt')
    failed_content_path = os.path.join(source_folder, 'failed_content.txt')

    # Count the total number of PDF files in the source_folder
    total_files = len([name for name in os.listdir(
        source_folder) if name.lower().endswith('.pdf')])

    # Initialize counters
    successful_extractions = 0
    failed_extractions = 0

    # Open (or create) the output file and overwrite if it already exists
    with open(output_file_path, 'w') as output_file, \
        open(failed_content_path, 'w') as failed_content_file, \
        open(csv_output_path, 'a', newline='') as csv_output_file, \
        open(csv_competency_unit_path, 'a', newline='') as csv_competency_unit_file:

        # Create CSV writers
        csv_writer = csv.writer(csv_output_file)
        csv_comp_unit_writer = csv.writer(csv_competency_unit_file)

        # Write the headers for the CSV files
        # csv_writer.writerow(
        #     ['Name', 'Qualification Code', 'Filename', 'Folder'])
        # csv_comp_unit_writer.writerow(
        #     ['Name', 'Qualification Code', 'Filename', 'Competency Unit', 'Folder'])
        
        # Write the source folder path at the beginning of the output file
        output_file.write(f"Source folder: {source_folder}\n\n")

        # Initialize a counter for the current file
        current_file = 0

        # Process each PDF file in the source_folder
        for filename in sorted(os.listdir(source_folder)):
            if filename.lower().endswith('.pdf'):
                current_file += 1  # Increment the current file counter
                pdf_path = os.path.join(source_folder, filename)
                # Print the file name with counters
                print(f'🔸 ({current_file}/{total_files}) Processing file: {filename}') 

                # Convert the specific page of the PDF into an image    
                try:
                    pages = convert_from_path(pdf_path, first_page=1, last_page=2, dpi=500)
                    text = ""
                    for page in pages:
                        text += pytesseract.image_to_string(page)

                    # Extract information
                    name = extract_name(text)
                    qualification_code = extract_qualification_code(text)
                    competency_units = extract_competency_unit(text)

                    if name:
                        output_file.write(f"{name}\n")
                        successful_extractions += 1
                        
                        if qualification_code:
                            print(
                                f"Extracted Data: '{name}' '{qualification_code}'")
                            csv_writer.writerow(
                                [name, qualification_code, filename[:-4], source_folder])

                        if competency_units:
                            for unit in competency_units:
                                csv_comp_unit_writer.writerow(
                                    [name, qualification_code, filename[:-4], unit, source_folder])

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
