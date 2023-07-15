

class FileArq:

    def __init__(self, open_:str) -> None:
        open_ = self.open
    
        print(open)
    #abre os arquivos que for passar.
    def open_arq(self, linha:bool=False, linhas:bool=False):
        ref_aqr = open("C:/Temp/Projeto/Gerador_doc/src/arquivos"+self.open,mode="r", encoding='UTF8')

        if ref_aqr == None:
            return None
        elif ref_aqr != None and linha==True:
            return ref_aqr.linha
        elif  ref_aqr!=None and linhas==True :
            return ref_aqr.linhas
        
        return ref_aqr
        

    