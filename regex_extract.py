import re

# Sample text from the OCR output
text = """
...
Certificate
NOMOR 5/0263240223/AS.01.04/II/2023
Diberikan Kepada :

This is to certify that :
Nama : MUSLIM
Name
Tempat, tanggal lahir +: _ PACITAN, 18-04-1996
...
"""

# Use regular expression to find the name
# match = re.search(r'Nama\s+:\s+([A-Z\s]+)', text)
match = re.search(r'Nama\s+:\s+([A-Z\s]+?)(?=\n|Name)', text)
if match:
    # The strip() function removes any leading/trailing whitespace
    name = match.group(1).strip()
    print(f"Extracted name: '{name}'")
else:
    print("Name could not be extracted.")


# Use regular expression to find the birthdate
match = re.search(
    r'Tempat,\s+tanggal\s+lahir\s+:\s+[A-Z\s]+,\s+(\d{2}-\d{2}-\d{4})', text)
if match:
    birthdate = match.group(1).strip()
    print(f"Extracted birthdate: '{birthdate}'")
else:
    print("Birthdate could not be extracted.")
