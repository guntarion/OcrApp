import pytesseract
from PIL import Image

# Set the path to the specific image file
file_path = '/Users/guntar/Documents/KerjaanPJB/Data/bahankerja/SCAN FFTC-SD PT MITRA KARYA 9-22 AGUSTUS031.jpg'

# Use pytesseract to do OCR on the image
text = pytesseract.image_to_string(Image.open(file_path))

# Output the extracted text to the console
print("Extracted Text:")
print("---------------")
print(text)
