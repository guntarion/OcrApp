import os

# Define the target folder
target_folder = 'E:/DataKerja/PENDING DJK 2021'

# Define the output file
output_file = 'DaftarFolderDgPDF.txt'

# Initialize an empty list to store the folders
folders_with_pdf = []

# Walk through the target folder
for root, dirs, files in os.walk(target_folder):
    # Check if any of the files end with .pdf
    if any(file.lower().endswith('.pdf') for file in files):
        # If so, add the root to the list of folders
        folders_with_pdf.append(root)

# Write the folders to the output file
with open(output_file, 'w') as file:
    for folder in folders_with_pdf:
        file.write(folder + '\n')