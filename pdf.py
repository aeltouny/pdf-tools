import PyPDF2 as pdf

with open('dummy.pdf' , 'rb') as file :
	reader = pdf.PdfReader(file)
	page = reader.pages[0]
	writer = pdf.PdfWriter()
	writer.add_page(page.rotate(90))
	with open('tilt.pdf' , 'wb') as file :
		writer.write(file)
