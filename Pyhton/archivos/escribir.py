with open('archivos\\texto','w',encoding="UTF-8") as archivo:
    #sobreescribiendo el archivo
    #archivo.write("Jajajajaa te la recontra teclee")
    
    #agregando 2 lineas con writelines
    archivo.writelines([" - Hola padre santo como andas\n"," - misericordia\n"])
    
    #agregando otras 2 lineas
    archivo.writelines([" - no se porque dijiste eso\n"," - yo tampoco"])