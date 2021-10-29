import PyPDF2

pdf_file = 'super.pdf'
watermark = 'wtr.pdf'
output = PyPDF2.PdfFileWriter()
input_file = open('super.pdf', 'rb')
input_pdf = PyPDF2.PdfFileReader(input_file)


water_file = open('wtr.pdf', 'rb')
water_pdf = PyPDF2.PdfFileReader(water_file)

for i in range(input_pdf.getNumPages()):
    page = input_pdf.getPage(i)
    page.mergePage(water_pdf.getPage(0))
    output.addPage(page)

    with open('merged.pdf', 'wb') as file:
        output.write(file)
