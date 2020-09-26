import pathlib
import PyPDF2

pdf_path = pathlib.Path('1.pdf')
with pdf_path.open('rb') as pdf_file:
    reader = PyPDF2.PdfFileReader(pdf_file, strict=False)
