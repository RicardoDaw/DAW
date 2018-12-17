try:
    palabra = input("Escribe lo que quieras:")
    vocales = "a","e","i","o","u"
    nueva_palabra = ""
    nueva_palabra1 = ""
    nueva_palabra3 = ""
     
    for letra in palabra:
        if letra in vocales:
            nueva_palabra += letra
    print ("Sin consonantes:", nueva_palabra)
            
    for letra in palabra:
        if not letra in vocales:
            nueva_palabra1 += letra
     
    print ("Sin vocales:", nueva_palabra1)
    
    for letra in palabra:
        if (letra in vocales):
            nueva_palabra3 += letra.upper()
        elif not letra in vocales:
                nueva_palabra3 += letra        
    print ("Vocales mayusculas: ", nueva_palabra3)
except:
    print ("Error, introduce una palabra")