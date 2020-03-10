from PyPDF2 import PdfFileReader, PdfFileWriter

output_dir = 'rotated\\'
file_name = 'DAA 5.pdf'

pdf_in = open('inputs\\'+file_name, 'rb')

pdf_reader = PdfFileReader(pdf_in)
pdf_writer = PdfFileWriter()

for page_num in range(pdf_reader.numPages):
    page = pdf_reader.getPage(page_num)
    page.rotateCounterClockwise(180)
    pdf_writer.addPage(page)

pdf_out = open(output_dir + file_name, 'wb')
pdf_writer.write(pdf_out)

pdf_out.close()
pdf_in.close()
