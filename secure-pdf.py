from PyPDF2 import PdfFileWriter, PdfFileReader
import sys

def secure_pdf(file, password):
    parser = PdfFileWriter()
    pdf = PdfFileReader(file)
    for page in range(pdf.numPages):
        parser.addPage(pdf.getPage(page))
    parser.encrypt(password)
    with open(f"secure_{file}", "wb") as f:
        parser.write(f)
        f.close()
    print(f"secure_{file} Created...")
    
if __name__ == "__main__":
    file = sys.argv[1]
    password = sys.argv[2]
    secure_pdf(file, password)