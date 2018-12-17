palabra = input("Escribe lo que quieras:")

a=0
for element in palabra:
    a+=1
    if element not in palabra[a:]:
        print (element,"=",end=" ")
        print(palabra.count(element),end="    ")