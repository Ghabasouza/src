from bs4 import BeautifulSoup 

class FileArq:

    def __init__(self, open_:str) -> None:
        self.open = open_ 
    
    #abre os arquivos que for passar.
    def open_arq(self):
        with open("C:/Projetos/Conversor/src/arquivos/"+self.open, "r") as f:
            Bs_data = BeautifulSoup(f.read(), "xml") 
        
        if Bs_data == None:
            return None
        elif Bs_data != None:
            return Bs_data
        

    def module_arq(self, Bs_data:BeautifulSoup):
        
        if Bs_data != None:
            data=[]
            b_unique = Bs_data.find_all('Module')
            
            for i in b_unique:
                if is_number(i):
                    data.append(i.next)
            
            return data
        else:
            return None
        
    def is_number(salf,num):
        try:
            float(num)
        except ValueError:
            return False
        return True