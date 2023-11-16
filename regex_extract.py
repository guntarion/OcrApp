import re

# Sample text from the OCR output
text = """
...
No Seri : 75834-27122021-01

RINCIAN UNIT KOMPETENSI (DETAILS FOR UNITS OF COMPETENCY)

A. Kompetensi Inti (Vain Competencies)

1. Unit Kompetensi (Unit Competency) : Mengkoordinir Pengoperasian Pembangkit Tenaga Listrik
(Coordinating the Operations of Power Plants)
Kode Unit (Code Unit) : D.35.114.00.077.1
2. Unit Kompetensi (Unit Competency) : Mengoperasikan Turbin Gas-Generator bagi Pelaksana Utama
(Operating Gas Turbine Generators for Primary Operators)
Kode Unit (Code Unit) : D.35.114.00.037.1

B. Kompetensi Pilihan (Optional Competencies)



...
"""

# Use regular expression to find the name
# match = re.search(r'Nama\s+:\s+([A-Z\s]+)', text)
# match = re.search(r'Nama\s+:\s+([A-Z\s]+?)(?=\n|Name)', text)
# if match:
#     # The strip() function removes any leading/trailing whitespace
#     name = match.group(1).strip()
#     print(f"Extracted name: '{name}'")
# else:
#     print("Name could not be extracted.")


# Use regular expression to find the birthdate
# match = re.search(
#     r'Tempat,\s+tanggal\s+lahir\s+:\s+[A-Z\s]+,\s+(\d{2}-\d{2}-\d{4})', text)
# if match:
#     birthdate = match.group(1).strip()
#     print(f"Extracted birthdate: '{birthdate}'")
# else:
#     print("Birthdate could not be extracted.")


# match = re.search(r': (.*?)(?=\n\n: \d{10,20})', text)
# if match:
#     name = match.group(1)
#     print(name)
# else:
#     print("Name could not be extracted.")

# mengambil kode kualifikasi (angka 3/4/5) dari string semacam D.35.114.01.KUALIFIKASI.3.KITTGU
pattern = r'KUALIFIKASI\.(\d)\.KIT[A-Za-z]+'
match = re.search(pattern, text)
if match:
    kode_kualifikasi = match.group(1)
    print(kode_kualifikasi)
else:
    print("Name could not be extracted.")

# mengambil info unit kompetensi
pattern = r'Unit Kompetensi \(Unit Competency\) : (.*)'
matches = re.findall(pattern, text)
for match in matches:
    print(match)
