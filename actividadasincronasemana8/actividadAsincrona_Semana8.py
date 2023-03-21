#Lista de paises  
pais1 = "el salvador"
pais2 = "mexico"
pais3 = "honduras"
pais4 = "nicaragua"
pais5 = "estados unidos"
pais6 = "españa"
pais7 = "japon"
pais8 = "argentina"
pais9 = "chile"
pais10 = "china"

#Lista de especies
especie1 = "canina"
especie2 = "felina"
especie3 = "porcina"
especie4 = "aves"
especie5 = "reptil"
especie6 = "anfibio"
especie7 = "insecto"
especie8 = "aracnido"
especie9 = "Molusco"
especie10 = "pez"

#Bienvenida
nombre = input("\nIngrese su nombre de usuario-> ")
print (f"Bienvenido/a {nombre}")



opcion = input('''
               \tMenu
               1- Humanos 
               2- Animales 
               Selecciona que opcion quieres -> ''').lower( )

if opcion == "Humanos" or opcion == "1":
    pais = input(f'''
                 \tMenu
                 1-{pais1}
                 2-{pais2}
                 3-{pais3}
                 4-{pais4}
                 5-{pais5}
                 6-{pais6}
                 7-{pais7}
                 8-{pais8}
                 9-{pais9}
                 10-{pais10}
                 
                 Ingrese el país del que desea conocer el gentilicio-> ''').lower()
     
    if pais == "El Salvador" or pais == "1":
        print (f"\nEl gentetilicio de {pais1} es 'Salvadoreño'")
    elif pais.lower() == "Mexico" or pais == "2":
        print (f"\nEl gentilicio de {pais2} es 'Mexicano'")
    elif pais.lower() == "Honduras" or pais == "3":
        print (f"\nEl gentilicio de {pais3} es 'Hondureño'")
    elif pais.lower() == "Nicaragua" or pais == "4":
        print (f"\nEl gentetilicio de {pais4} es 'Nicaraguence'")
    elif pais.lower() == "Estados Unidos".lower() or pais == "5":
        print (f"\nEl gentetilicio de {pais5} es 'Estadounidene'")
    elif pais.lower() == "España".lower() or pais == "6":
        print (f"\nEl gentetilicio de {pais6} es 'Español'")
    elif pais.lower() == "Japon".lower() or pais == "7":
        print (f"\nEl gentetilicio de {pais7} es 'Japones'")
    elif pais.lower() == "Argentina".lower() or pais == "8":
        print (f"\nEl gentetilicio de {pais8} es 'Argentino'")
    elif pais.lower() == "Chile".lower() or pais == "9":
        print (f"\nEl gentetilicio de {pais9} es 'Chileno'")
    elif pais.lower() == "China".lower() or pais == "10":
        print (f"\nEl gentetilicio de {pais10} es 'Chino'")
    else:
        print("El país ingresado no se encuentra en el programa.")

elif opcion.lower() == "Animales".lower() or opcion == "2":
    especie = input(f'''
                    \tMenu
                    1-{especie1}
                    2-{especie2}
                    3-{especie3}
                    4-{especie4}
                    5-{especie5}
                    6-{especie6}
                    7-{especie7}
                    8-{especie8}
                    9-{especie9}
                    10-{especie10}
                    
                    Ingrese la especie de la que desea conocer el animal -> ''')
    
    if especie.lower() == "Canina".lower():
        print (f"\nEl animal de la especie {especie1} es 'Perro'")
    elif especie.lower() == "Felina".lower():
        print (f"\nEl animal de la especie {especie2} es 'Gato'")
    elif especie.lower() == "Porcina".lower:
        print (f"\nEl animal de la especie {especie3} es 'Cerdo'")
    elif especie.lower() == "Aves".lower():
        print (f"\nEl animal de la especie {especie4} es 'Águila'")
    elif especie.lower() == "Reptil".lower():
        print (f"\nEl animal de la especie {especie5} es 'Cocodrilo'")
    elif especie.lower() == "Anfibio".lower():
        print (f"\nEl animal de la especie {especie6} es'Rana'")
    elif especie.lower() == "Insecto".lower():
        print (f"\nEl animal de la especie {especie7} es 'Abeja'")
    elif especie.lower() == "Arácnido".lower():
        print (f"\nEl animal de la especie {especie8} es 'Araña'")
    elif especie.lower() == "Molusco".lower():
        print (f"\nEl animal de la especie {especie9} ess 'Pulpo'")
    elif especie.lower() == "Pez".lower():
        print (f"\nEl animal de la especie {especie10} es 'Tiburón'")
    else:
        print("La especie ingresada no se encuentra en el programa.")

else:
    print ("Opción inválida")
    
print ("\nFin de la actividad, gracias por participar :)")