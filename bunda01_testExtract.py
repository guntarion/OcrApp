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
    pattern = r'\n[>:-]\s*([A-Za-z\s]+)'
    match = re.search(pattern, text)
    if match:
        return match.group(1).strip()

    return None


# Set the source folder
# source_folder = 'E:\OneDrive\Documents\WorkingFiles\PENDING DJK 2021\PENDING - 0921 Sertifikasi DJK\Batch 1_UBJOM PULPIS'
source_folder = r"E:\JAPOGdrive\My Drive\01 PT JTB Projects\001 Sertifikat PJCA\Raw Mat Bahan Sertifikat\Box Pembelajaran Teknik\Jar Teknik 2021\PENDING - 1221 Sertifikasi DJK Desember 2021 Batch 1 dan 2\Sertifikat(17)\Sertifikat\\"

# Set the filename manually
filename = 'Binder1_02.pdf'

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
        print(f"✅ Extracted name: '{name}'")
    else:
        print("🧨 Name could not be extracted.")
else:
    print("Could not read the specified page from the PDF file.")

print('✨ Finished OCR processing and name extraction from the PDF file.')
