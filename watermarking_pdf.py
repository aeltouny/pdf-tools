import PyPDF2 as pdf
import argparse , os

parser = argparse.ArgumentParser()

parser.add_argument(
        dest="wtr", 
        type=str, 
        help="Please specifiy the watermark pdf"
    )

parser.add_argument(
        dest="pdfs", 
        type=str, 
        nargs='+',
        help="Please specifiy the names of the PDFs seprated by space"
    )


args = parser.parse_args()

#Check if watermark pdf is exist
if not os.path.exists(args.wtr) :
        print(f"{args.wtr} file is not exist")
else:
        with open( args.wtr , 'rb') as wtrmark_file :
                wtrmark_reader = pdf.PdfReader(wtrmark_file)
                wtrmark_page = wtrmark_reader.pages[0]

                for pdf_file in args.pdfs :
                        if not os.path.exists(pdf_file) :
                                print(f"{pdf_file} is not exist")
                        else:
                                #Instantiate writer object
                                writer = pdf.PdfWriter()
                                with open(pdf_file , 'rb') as file :
                                        pdf_reader = pdf.PdfReader(file)
                                        for page_num in range(len(pdf_reader.pages)):
                                                content_page = pdf_reader.pages[page_num]
                                                content_page.merge_page(wtrmark_page)
                                                writer.add_page(content_page)
                        with open(pdf_file[:-4]+'_watermarked.pdf', 'wb') as result_file:
                                writer.write(result_file)

