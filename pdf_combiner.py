import PyPDF2 as pdf
import argparse , os

parser = argparse.ArgumentParser()

parser.add_argument(
        dest="pdfs", 
        type=str, 
        nargs='+',
        help="Please specifiy the names of the PDFs seprated by space"
    )


args = parser.parse_args()

mergedObject = pdf.PdfMerger()

# Loop on the pdfs and check if they are valid files 
for pdf_file in args.pdfs :
        if not os.path.exists(pdf_file) :
                print(f"{pdf_file} is not exist")
        else:
                #with open(pdf_file , 'rb') as file :
                        #reader = pdf.PdfReader(file)
                        #mergedObject.append(reader)
                mergedObject.append(pdf_file)
mergedObject.write("mergedfiles.pdf")



