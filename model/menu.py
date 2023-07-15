

class Menu: 
    
    def __init__(self, module:str, title_menu:str, title:str, function:str):
        self.module = module
        self.title_Menu = title_menu
        self.title = title  
        self.Function = function
        
    def Get_Module(self):
        return self.module
    def Set_Module(self, module):
        self.module = module
    
    def Get_titlle_menu(self):
        return self.title_Menu
    def Set_title_menu(self, title_menu):
        self.title_Menu = title_menu
    
    def Get_title(self):
        return self.title
    def Set_title(self, title):
        self.title = title

    def Get_function(self):
        return self.Function
    def Set_function(self, function):
        self.function = function