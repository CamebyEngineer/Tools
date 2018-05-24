#! /usr/bin/python3

from PyPDF2 import PdfFileWriter, PdfFileReader

def watermarks(temp, watermar,new_file):
    template = PdfFileReader(open(temp, 'rb'))
    wpdf = PdfFileReader(open(watermar, 'rb'))
    watermark = wpdf.getPage(0)
    output = PdfFileWriter()

    for i in range(template.getNumPages()):
        page = template.getPage(i)
        page.mergePage(watermark) #.rotateCounterClockwise(90))
        output.addPage(page.rotateClockwise(90))

        with open(new_file, 'wb') as f:
            output.write(f)



pdflist = ["Seam Period Progress Plot By Year KG1.pdf",
           "Seam Period Progress Plot By Year KG2.pdf",
            "Seam Period Progress Plot By Year KG3.pdf",
            "Seam Period Progress Plot By Year KG4.pdf",
            "Seam Period Progress Plot By Year MA1.pdf",
            "Seam Period Progress Plot By Year MA1U.pdf",
            "Seam Period Progress Plot By Year MA2B.pdf",
            "Seam Period Progress Plot By Year MA2T.pdf",
            "Seam Period Progress Plot By Year MA3.pdf",
            "Seam Period Progress Plot By Year MA3U.pdf",
            "Seam Period Progress Plot By Year MA4.pdf",
            "Seam Period Progress Plot By Year NG1L.pdf",
            "Seam Period Progress Plot By Year NG1U.pdf",
            "Seam Period Progress Plot By Year NG2.pdf",
            "Seam Period Progress Plot By Year NG3.pdf",
            "Seam Period Progress Plot By Year NG4.pdf",
            "Seam Period Progress Plot By Year NG5.pdf",
            "Seam Period Progress Plot By Year NG6.pdf",
            "Seam Period Progress Plot By Year NG7.pdf",
            "Seam Period Progress Plot By Year KG Seam Group.pdf",
            "Seam Period Progress Plot By Year MA Seam Group.pdf",
            "Seam Period Progress Plot By Year NG Seam Group.pdf"]

for pdf in pdflist:
    watermarks("Legend.pdf", pdf, f"MAjorEa\\{pdf}" )

