from bs4 import BeautifulSoup 
from model.menu import Menu
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
        
    def is_number(self,num):
        try:
            float(num.next)
        except ValueError:
            return False
        return True

    def module_arq(self, Bs_data:BeautifulSoup):
        
        if Bs_data != None:
            b_unique = Bs_data.find_all('Module')
            
            if not self.is_number(b_unique[0]):

                return b_unique[0].next
            else:
                return None
        
        
    def menu_title_sub(self, Bs_data:BeautifulSoup):
        
       if Bs_data != None:
           data=[]
           b_unique = Bs_data.find_all('Title', {'lang':'pt'})
           for i in b_unique:
               data.append(i.next)