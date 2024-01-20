import os
from pdf2image import convert_from_path
import pytesseract
import re



# Set the source folder
# source_folder = 'E:\OneDrive\Documents\WorkingFiles\PENDING DJK 2021\PENDING - 0921 Sertifikasi DJK\Batch 1_UBJOM PULPIS'
source_folder = r"C:\MyCodes\Django\48KaryaInovasiPLN\DataContoh\\"

# Set the filename manually
filename = '11-NTS.34-Kantor Pusat-Optimalisasi Aplikasi Monitoring Online (RINGG ON).pdf'

# Set the page where the data is located
data_location = 2  # Change this as needed

# Combine the source folder and file name
pdf_path = os.path.join(source_folder, filename)
print(f'Processing file: {filename}')

# Convert all pages of the PDF into images
pages = convert_from_path(pdf_path, dpi=500)

# Set the output file name
output_filename = os.path.splitext(filename)[0] + '.txt'

# Set the output file path
output_path = os.path.join(source_folder, output_filename)

# Define the phrases to be surrounded
phrases = ["Latar Belakang", "Maksud dan Tujuan", "Identifikasi Masalah", "Analisis Penyelesaian Masalah",
           "Metodologi", "Desain Karya Inovasi", "Evaluasi Hasil Implementasi", "Hasil dan Pembahasan", "Kesimpulan", "Saran", "Daftar Pustaka", "Lampiran"]

# Open the output file in write mode
with open(output_path, 'w', encoding='utf-8') as f:
    # Loop over all pages
    for i, page in enumerate(pages, start=1):
        print(f'Processing page {i}...')

        # OCR the image and output all text
        text = pytesseract.image_to_string(page)

        # Remove line breaks that are not followed by a capital letter
        text = re.sub(r'\n(?![A-Z]|I{1,3}|IV|IX|V?I{0,3}\.|[a-z]\.|[0-9]\.|-)', ' ', text)

        # Surround the phrases with [[ and ]] and add a double line break after them
        for phrase in phrases:
            text = re.sub(fr'(?i)\b{phrase}\b', f'[[{phrase}]]\n\n', text)

        # Write the text to the output file
        f.write(text + '\n\n--- End of Page ---\n\n')

print(f'✨ Finished OCR processing and extraction from the PDF file. Output saved to {output_path}.')
