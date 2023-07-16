from model.menu import Menu
from controller.file import FileArq
import json 


  

teste = FileArq('fatvenda.xml')
#t = teste.module_arq(teste.open_arq())
tes = teste.menu_title_sub(teste.open_arq())
print(tes)