import PyPDF2 ### !pip install PyPDF2

def paginar(path:str):

    ### leitura do conteudo contido no arquivo PDF
    obj = open(path, "rb")
    
    ### criando uma nova instancia da classe PyPDF2.PdfReader()
    pdf = PyPDF2.PdfReader(obj)

    ### criando um objeto dict para registrar os pares de "chave : valor"
    ### chave = numero da pagina PDF | valor = texto contido na respectiva pagina
    paginas = {}
    
    ### iteracao sob todas as paginas existentes no arquivo de forma dinamica 
    for i in range(0, len(pdf.pages)):

        ### pagina referente ao respectivo valor de "i" na iteracao
        page = pdf.pages[i]
        
        ### extracao do texto contido na pagina da iteracao
        text = page.extract_text().replace("\n", " ")

        ### adicionando o par de "chave:valor" referente ao index:texto da iteracao
        paginas[i] = text
        
    
    return paginas

