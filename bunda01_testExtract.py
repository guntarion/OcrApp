import os
from pdf2image import convert_from_path
import pytesseract
import re


def extract_name(text):
    # First pattern to capture text between "Nama (Name) :" and "Nomor NIK/Paspor"
    first_pattern = r'Nama \(Name\) :\s*([^\n]+)'

    # Try the first pattern
    first_match = re.search(first_pattern, text, re.IGNORECASE)
    if first_match:
        return first_match.group(1).strip()

    # If the first pattern didn't match, then use the alternative pattern
    # This pattern finds lines that are likely to contain the name, then processes them
    lines = text.split('\n')
    for i, line in enumerate(lines):
        if ':' in line or '-' in line:
            # Check if the next line has a colon and a number
            if i + 1 < len(lines) and re.match(r': \d{10,20}', lines[i + 1]):
                # Extract the name from the current line
                name_match = re.search(r'(?<=[:\-] )([^\n:]+)', line)
                if name_match:
                    return name_match.group(1).strip()
    return None


# Set the source folder
source_folder = '/Users/guntar/Downloads/PENDING DJK 2021/PENDING - 0921 Sertifikasi DJK/Batch 1_UBJOM PULPIS'

# Set the filename manually
filename = 'Scan Sertifikat PT PJB UBJOM PLTU Pulang Pisau (1)_14.pdf'

# Set the page where the data is located
data_location = 2  # Change this as needed

# Combine the source folder and file name
pdf_path = os.path.join(source_folder, filename)
print(f'Processing file: {filename}')

# Convert the specific page of the PDF into an image
pages = convert_from_path(
    pdf_path, first_page=data_location, last_page=data_location, dpi=500)
if pages:  # Check if the list of pages is not empty
    page = pages[0]

    # OCR the image and output all text
    text = pytesseract.image_to_string(page)
    print(text)
    print("\n--- End of Page ---\n")

    # Attempt to extract the name
    name = extract_name(text)
    if name:
        print(f"Extracted name: '{name}'")
    else:
        print("Name could not be extracted.")
else:
    print("Could not read the specified page from the PDF file.")

print('Finished OCR processing and name extraction from the PDF file.')
