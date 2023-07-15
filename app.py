#from model.menu import Menu
from controller.file import FileArq
import json 

def read ():
    ref_arquivo = FileArq("fatvenda.xnu")
    read = ref_arquivo.read
    print(read)
    teste = json.dump(read) 
    linha = ref_arquivo.read()
    while linha:
        valores = linha.split()
        print('QB ', valores[0], valores[1], 'obteve a avaliacao ', valores[10] )

    ref_arquivo.close()
        
read()