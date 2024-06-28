#!/usr/bin/env python
# coding: utf-8

# # MENÚ DE PELÍCULAS (PROYECTO DEL CAMPUS SENIOR DE PYTHON)

# ## PROGRAMACIÓN POR DANIEL GARCÍA

# In[164]:


fin = 0
peliculas = {'todas': ['Sonic la película', 'Sonic 2 la película', 'Spiderman', 'Sonic 3',
                       "Super Mario Bros. La película", 'Avengers: Infinity War', 'Avengers: Endgame',
                       'Los juegos del hambre', 'Shrek 2', 'El castillo ambulante']} 
vistas = {'Sonic la película': ['14-02-2020', '31-03-2020'], 'Sonic 2 la película': ['01-04-2022', '08-04-2022'],
           'Spiderman': ['15-03-2024'],"Super Mario Bros. La película": ['05-04-2023'], 
           'Avengers: Infinity War': ['30-04-2018'], 'Avengers: Endgame': ['26-04-2018'],
            'Los juegos del hambre': ['21-05-2024'] } 
no_vistas = ['Shrek 2', 'El castillo ambulante']
veces = { 'Sonic la película': 9, 'Sonic 2 la película': 9,
           'Spiderman': 1,"Super Mario Bros. La película": 4, 
        'Avengers: Infinity War': 1, 'Avengers: Endgame': 1,
            'Los juegos del hambre': 1 }
#MENÚ:
#1.Ver todas las pelis (con solo títulos)
def VerPelis():
    print ("\nPelículas en tu lista:\n",peliculas['todas'])
#2.Ver todas las pelis (con fechas)
def VerPelisFechas ():
    print (vistas)
#3.Ver pelis que no se han visto
def VerPelisNoVistas():
    print (no_vistas)
#4.Ver veces que se ha visto una película
def VerVeces ():
    print (veces)
#5.Añadir pelis
def AnadirPelis():
    añadir = input("\nEscribe el nombre de la película que vas a añadir\n")
    vista = (input ("¿La has visto?\n")).lower()
    if vista == 'si' or vista == 'sí':
        fecha = input ("Pon la fecha en la que la has visto\n")
        vec = input ("¿Cuantas veces la has visto?\n")
        (peliculas['todas']).append(añadir)
        vistas[añadir] = [fecha]
        veces[añadir] = [vec]
    else:
        (peliculas['todas']).append(añadir)
        no_vistas.append(añadir)
#6.Eliminar
def Eliminar ():
    basura = input("\nEscribe el nomnbre de la pelicula que quieres eliminar:\n")
    (peliculas['todas']).remove (basura)
    if basura in vistas.keys(): 
        vistas.pop (basura)
        veces.pop (basura)
    elif basura in no_vistas: 
        no_vistas.remove(basura) 
    
#7.Marcar como vista
def Marcar ():
    viste = input  ("\nEscribe el nombre de la pelicula que ya has visto (tiene que estar en la lista de peliculas no vistas)\n")
    vez = input ("¿Cuantas veces has visto "+ viste + "?\n")
    fec = input ("Cuando viste "+ viste +"?\n")
    if viste in no_vistas:
        no_vistas.remove(viste)
        (peliculas['todas']).append(viste)
        veces[viste] = vez
        vistas[viste] = [fec]
    elif not (viste in no_vistas):
        print (viste,"no está en la lista")
#8.Salir
def Salir ():
    print ("Saliendo...")
    fin = 1
#MENÚ
def ImprimirMenu ():
    print("     ____  ________    ____________  ____    ___   _____")
    print("    / __ \/ ____/ /   /  _/ ____/ / / / /   /   | / ___/")
    print("   / /_/ / __/ / /    / // /   / / / / /   / /| | \__ \ " )
    print("  / ____/ /___/ /____/ // /___/ /_/ / /___/ ___ |___/ /") 
    print(" /_/   /_____/_____/___/\____/\____/_____/_/  |_/____/" ) 
                                                       
    print ("\n\nMENU")
    print ("------------------------------------------------")
    print ("1.Ver todas las pelis ( con fechas incluidas )")
    print ("2. Ver todas las pelis ( solo titulos )")
    print ("3.Ver pelis que no se han visto")
    print ("4.Ver veces que se ha visto una película")
    print ("5.Añadir pelis")
    print ("6.Eliminar")
    print ("7.Marcar como vista")
    print ("8.Salir")
    print ("------------------------------------------------\n\n")
    opcion = input ("¿Qué opción quiere realizar ")
    opcion = int (opcion)
    if opcion == 1:
        VerPelisFechas ()
        ImprimirMenu ()
    elif opcion == 2:
        VerPelis ()
        ImprimirMenu ()
    elif opcion == 3:
        VerPelisNoVistas ()
        ImprimirMenu ()
    elif opcion == 4:
        VerVeces ()
        ImprimirMenu ()
    elif opcion == 5:
        AnadirPelis ()
        ImprimirMenu ()
    elif opcion == 6:
        Eliminar ()
        ImprimirMenu ()
    elif opcion == 7:
        Marcar ()
        ImprimirMenu ()
    elif opcion == 8:
        Salir ()
    elif opcion == 9 or opcion < 9 or opcion == 0 or opcion < 0:
        print ("Opción no valida\n\n")
        ImprimirMenu ()
    else:
        print ("Opción no valida\n\n")
        ImprimirMenu ()


# In[130]:


VerPelis()


# In[131]:


VerPelisFechas()


# In[138]:


VerPelisNoVistas ()


# In[133]:


AnadirPelis()


# In[134]:


VerVeces ()


# In[135]:


Eliminar ()


# In[137]:


Marcar ()


# In[ ]:


ImprimirMenu ()

