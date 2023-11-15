import re

# Sample text from the OCR output
text = """
...
Wa

- cons a
Advancing Competency of Power Generatic

PT .SERTIFIKAS| KOMPETENS! PEMBANGKITAN TENAGALISTRIK a.

JI. Tebet Raya No.44D - Tebet, Jakarta Selatan Ny
Telepon : (021) 22831822, Website : www.ptskp.id Email : ptskp@ptskp.id —
SNITISO 900] 2015

No Serthkat 0572-M

Akreditasi Menteri Energi dan Sumber Daya Mineral Nomor : 13 Stf/20/DJL.4/2017 Tanggal : 22 Agustus 2017
Minister of Energy and Mineral Resources Accreditation Number : 13 Stf/20/DJL.4/2017 Date: 22th August 2017

Sertifikat Kompetensi - Certificate of Competency

Nomor Sertifikat (Certificate Number) : 1630.0.07.P054.09.2021
Nomor Registrasi (Registration number) : 48898.1.2021

Dengan ini menyatakan bahwa (This is certify that)

Nama (Name)

Nomor NIK/Paspor (/dentity Number/Passport Number)
Tempat dan Tanggal Lahir (Place and Date of Birth)
Alamat (Address)

Telah dinyatakan kompeten dalam (Has been declared the competent in)

Jabatan/Profesi (Occupational/Professional)
Deskripsi Jabatan/Profesi (Occupational/Professional Description)

Kode Jenjang Kualifikasi (Code Level Qualification)

No Seri : 48898-01102021-01

: Bagus Setiawan

: 3578291708910001

: Surabaya, 17 Agustus 1991

: Kedung Cowek 4/24-b Kel. Kedung Cowek, Kec. Bulak Kota Surabaya Provinsi Jawa Timur

: Supervisor Junior Pemeliharaan Boiler

(Junior Boiler Maintenance Supervisor)

: Melaksanakan pekerjaan supervisi pemeliharaan boiler pada PLTU

(Supervising the Maintenance of Boilers on Steam Power Plants)

> D.35.115.01.KUALIFIKASI.4.KITLTU

Ditetapkan di (Defined in) Jakarta
Pada tanggal (At the date of) 30 September 2021
Nama LSK (Name LSK) PT. SKP Tenaga Listrik

Nama Penandatanggn (Signatory name) : Mudjiono
Jabatan (Position) : Direktur

Sertifikat Kompetensi ini berlaku selama 3 (tiga) tahun sejak tanggal dikeluarkan
(Certificate of Competence is valid for three (3) years from the date of issuance)

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


match = re.search(r': (.*?)(?=\n\n: \d{10,20})', text)
if match:
    name = match.group(1)
    print(name)
else:
    print("Name could not be extracted.")
