

class FileArq:

    def __init__(self, open:str) -> None:
        open = self.open
    
    #abre os arquivos que for passar.
    def open_arq(self, open:str):
        ref_aqr = open("C:/Temp/Projeto/Gerador_doc/src/arquivos"+open,mode="r", encoding='UTF8')

        if ref_aqr != None:
            return ref_aqr
        else:
            return None
        
    def json_arq(self):

        open_arq(open)

    