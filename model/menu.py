

class Menu: 
    
    def __init__(self, module:str, title_Menu:str, title:str, function:str):
        self.module = module
        self.title_Menu = title_Menu
        self.title = title  
        self.Function = function
        
    def Get_Module(self):
        return self.module
    
    
    def Set_Module(self, module):
        self.module = module