#IF ELSE Y SU EXPLICACION 

edad = 11
if edad >= 18:
    print('Eres mayor de edad y puedes pasar')
else:
    print('Eres menor de edad y no puedes pasar')   
    
   ##Seugunda forma de hacerlo
    contraseña_almacenada = "SkereMandela"
contraseña_escrita = '''SkereMandelaa'''

if contraseña_almacenada == contraseña_escrita:
    print('Contraseña correcta')    
else:
    print('Contraseña incorrecta o no existe, llama a soporte')
    


## Else if y tambien If anidados

ingreso_mensual = 120000
gasto_mensual = 90000


if ingreso_mensual > 10000:
    if ingreso_mensual - gasto_mensual < 0: 
        print("estas en deficit")
    elif ingreso_mensual - gasto_mensual > 3000:
        print("bien estas algo mejor que muchas personas, estas bien")
    else:
        print("y hermano, estas gastando mucho, hay que ver si te alcanza")
    
elif ingreso_mensual > 1000:
    print("estas bien en latinoamerica")
    
elif ingreso_mensual > 800:
    print("estas bien en Mexico")
    
elif ingreso_mensual > 140:
    print("estas bien en Tuxtepec")
    
else: 
    print("Eres  pobre")
    
## Esto funciona si la primera condicion no se cumple nos vamoos al else, pero si la principal
# condicion no se cumple se ira en escalera hasta que se cumpla alguna condicion