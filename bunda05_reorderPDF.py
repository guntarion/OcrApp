import os
from PyPDF2 import PdfReader, PdfWriter

source_folder = '/Users/guntar/Downloads/PENDING DJK 2021/PENDING - 0921 Sertifikasi DJK/Tes/'
target_folder = '/Users/guntar/Downloads/PENDING DJK 2021/PENDING - 0921 Sertifikasi DJK/TesHasil/'

# Get a list of all PDF files in the source folder
pdf_files = [f for f in os.listdir(source_folder) if f.endswith('.pdf')]

# Sort the list of PDF files in alphabetical order
pdf_files.sort()

for pdf_file in pdf_files:
    # Open the PDF file
    with open(os.path.join(source_folder, pdf_file), 'rb') as file:
        reader = PdfReader(file)

        # Ensure the PDF has at least 2 pages
        if len(reader.pages) < 2:
            print(f"Skipping {pdf_file} as it has less than 2 pages")
            continue

        writer = PdfWriter()

        # Add the second page first
        writer.add_page(reader.pages[1])

        # Then add the first page
        writer.add_page(reader.pages[0])

        # Define the output file path
        output_file_path = os.path.join(target_folder, 'S_' + pdf_file)

        # Write the reordered pages to a new PDF file
        with open(output_file_path, 'wb') as output_file:
            writer.write(output_file)