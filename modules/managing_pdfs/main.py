# PyPDF2 for manipulating PDF files
# doc: https://pypdf2.readthedocs.io/en/3.0.0/
from pathlib import Path
from PyPDF2 import PdfReader, PdfWriter, PdfMerger

ROOT_FOLDER = Path(__file__).parent
ORIGINAL_FOLDER = ROOT_FOLDER / 'original'
NEW_FOLDER = ROOT_FOLDER / ' new_folder'

BACEN_REPORT = ORIGINAL_FOLDER / 'R20231215.pdf'

NEW_FOLDER.mkdir(exist_ok=True)

reader = PdfReader(BACEN_REPORT)

# print(len(reader.pages))
# for page in reader.pages:
#     print(page)
#     print()

page0 = reader.pages[0]
image0 = page0.images[0]

# print(page0.extract_text())

# with open(NEW_FOLDER / image0.name, 'wb') as fp:
#     fp.write(image0.data)

# writer = PdfWriter()

# writer.add_page(page0)
# with open(NEW_FOLDER / 'page0.pdf', 'wb') as file:
#     writer.write(file)

# with open(NEW_FOLDER / 'new_pdf.pdf', 'wb') as file:
#     for page in reader.pages:
#         writer.add_page(page)
#     writer.write(file)

# for i, page in enumerate(reader.pages):
#     writer = PdfWriter()
#     with open(NEW_FOLDER / f'page{i}.pdf', 'wb') as file:
#         writer.add_page(page)
#         writer.write(file)

merger = PdfMerger()

files =  [
    NEW_FOLDER / 'page1.pdf',
    NEW_FOLDER / 'page0.pdf',
]

for file in files:
    merger.append(file)

merger.write(NEW_FOLDER / 'inverted.pdf')
merger.close()