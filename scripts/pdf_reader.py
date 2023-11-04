import PyPDF2
 
def paginar(path:str):

    pages = {}
        
    with open(path, "rb") as file:
        
        pdf = PyPDF2.PdfReader(file)
   
        for num in range(0, len(pdf.pages)):
            pages[num] = pdf.pages[num].extract_text() 
            

    return pages


