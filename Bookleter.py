
###############Pdf2Booklet2021 -V.2.02################
#	       Develope by Md Nishu Ahmad                #
#           CopyRight Resereved                      #
#                                                    #
######################################################


from PyPDF2 import PdfFileReader, PdfFileWriter, PdfFileMerger
import os


def deleteBuffer(file_base_name):
    print("Deleting Buffer")
    if os.path.exists('./blankPage/'+file_base_name+'.pdf'):
        # print("Deleting...."+str(NumFile))
        os.remove('./blankPage/'+file_base_name+'.pdf')


def reverse(file_base_name):
    print("reversing...")
    path = './booklet/'+file_base_name+'.pdf'
    pdf = PdfFileReader(path)

    output_pdf = PdfFileWriter()
    for page in reversed(pdf.pages):
        output_pdf.addPage(page)

    with open(r'./booklet/'+file_base_name+'.pdf', "wb") as writefile:
        output_pdf.write(writefile)
        writefile.close()


def arrange(b, index, file_base_name):
    print("Arraging")
    path = './blankPage/'+file_base_name+'.pdf'
    pdf = PdfFileReader(path)
    Pages = pdf.getNumPages()-1
    Last = Pages

    if index == 2:
        L_1 = Pages-b+1
    elif index == 1:
        L_1 = Pages-b
    else:
        L_1 = Pages-b+2

    output_pdf = PdfFileWriter()

    for page in range(Pages+1):
        if page == L_1:
            output_pdf.addPage(pdf.getPage(Last))

        elif page == Last:
            output_pdf.addPage(pdf.getPage(L_1))
        else:
            output_pdf.addPage(pdf.getPage(page))

    with open(r'./blankPage/'+file_base_name+'.pdf', "wb") as writefile:
        output_pdf.write(writefile)
        writefile.close()


def AddBlank(Blanks, pdf, file_base_name):
    print("Running AddBlank")
    pdf_writer = PdfFileWriter()
    pdf_writer.addBlankPage(200, 200)
    with open('_blank_Page.pdf', 'wb') as f:
        pdf_writer.write(f)
        f.close()

    blank = PdfFileReader('_blank_Page.pdf')
    merger = PdfFileMerger()
    merger.append(pdf)
    if Blanks != 4:
        for i in range(Blanks):
            print("AddingBlank", i)
            merger.append(blank)
        # pdfs = [pdf_file_path, '_blank_Page.pdf',]
    merger.write('./blankPage/'+file_base_name+'.pdf')
    # with open(os.path.join(output_folder_path_blank,'{0}.pdf'.format(file_base_name)),'wb') as f:
    merger.close()
    # merger.close()


def sortingPdf(Pages, file_base_name):
    print('Sorting')
    output_pdf = PdfFileWriter()

    Total = Pages
    Forth_Total = Total//4
    initial = 1
    j = 1
    with open(r'{0}.pdf'.format('./blankPage/'+file_base_name), 'rb') as readfile:

        input_pdf = PdfFileReader(readfile)

        print()
        for page in range(initial, Forth_Total+1):
            print("loop-", page)
            output_pdf.addPage(input_pdf.getPage(j))
            output_pdf.addPage(input_pdf.getPage(Total-2))
            output_pdf.addPage(input_pdf.getPage(Total-1))
            output_pdf.addPage(input_pdf.getPage(j-1))
            print("normal", '{0},{1},{2},{3}'.format(j+1, Total-1, Total, j))
            j += 2
            Total -= 2

        with open(r'./booklet/'+file_base_name+'.pdf', "wb") as writefile:
            output_pdf.write(writefile)
    print("Complete Sorting")


def CreatingFolder():
    path1 = 'booklet'
    path2 = 'blankPage'

    try:
        os.mkdir(path1)
        os.mkdir(path2)

        print("Folder CReated")
    except OSError as error:
        pass


def main():

    # Create two folder
    CreatingFolder()

    name = input("Enter File name-")+'.pdf'
    # import pdf file
    # name='HTML Tutorial.pdf'

    inpt = input("Enter 'Y' or 'y' for Reverse:-")
    pdf = PdfFileReader(name)
    Pages = pdf.getNumPages()
    blanks = 4-(Pages % 4)
    print('blanker-', blanks)
    file_base_name = name.replace('.pdf', '')
    # pdf=PdfFileReader(name)
    index = blanks
    AddBlank(blanks, name, file_base_name)

    if index != 4:

        for i in range(blanks):
            print(i)
            arrange(blanks, index, file_base_name)
            blanks += 1
    else:
        index = 0

    # Total pages_after Adding Blanks=Pages_before+No_of Blanks
    sortingPdf(Pages+index, file_base_name)

    if inpt == 'y' or inpt == 'Y':

        reverse(file_base_name)

    deleteBuffer(file_base_name)
    print(input("Enter any key to 'exit'!"))


if __name__ == "__main__":
    # calling the main function
    main()
