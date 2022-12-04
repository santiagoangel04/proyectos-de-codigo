#archivo pdf encriptado
from PyPDF2 import PdfFileWriter, PdfFileReader
out=PdfFileWriter()
file=PdfFileReader(input("ingrese el archivo: "))
num=file.numPages
for idx in range(num):

    page=file.getPage(idx)

    out.addPage(page)

out.encrypt(input("escriba un pin: "))

with open("archivo_encriptado.pdf","wb") as f:


    out.write(f)
