from PyPDF2 import PdfFileReader, PdfFileWriter
pdf_file_path = 'file1.pdf'
pdf = PdfFileReader(pdf_file_path)

pdfwriter = PdfFileWriter()

for page_num in range(2,6):
    pdfwriter.addPage(pdf.getPage(page_num))

with open('newoutput.pdf',"wb") as out:
    pdfwriter.write(out)
print("PDF file has been split")
