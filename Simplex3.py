import numpy

#Zeilfunktionseingabe muss noch überarbeitet werden

############################################################
#x = int(input('Wie viele Strukturvariablen hat die Aufgabenstellung: '))+1
#y = int(input('Wie viele Nebenbedingungen hat die Aufgabenstellung: '))+1
x=3
y=4
############################################################
#x+1 für b                   y+1 für Zielfunktion

#erstellen des Arrays
array=numpy.zeros((y,x))
#verhindert die exponentielle Darstellung (e-2 usw)
numpy.set_printoptions(suppress=True)
#Nachkommastellen auf 4 begrenzen
numpy.set_printoptions(precision=4)


############################################################
#Entwicklungszweck array
array3=numpy.zeros((4,3))
#array3=numpy.float((4,3))
array3[[0],[0]]=40
array3[[0],[1]]=24
array3[[0],[2]]=480
array3[[1],[0]]=24
array3[[1],[1]]=48
array3[[1],[2]]=480
array3[[2],[0]]=0
array3[[2],[1]]=60
array3[[2],[2]]=480
array3[[3],[0]]=10
array3[[3],[1]]=40
array3[[3],[2]]=1
############################################################




#eigentlicher Simplex
def simplex(array,ele,stelle):
    #teilen der Pivot Zeile durch Pivotelement
    teiler = array[[ele],[stelle]]
    for i in range(0,len(array)+2):
        array[[ele],[i]]=array[[ele],[i]]/teiler
    print(array)


    #neutralisieren der Objekte in der Pivot Spalte
    for i in range(0, y):
        multi = array[[i],[stelle]]
        #print("multi = "+str(multi))
        for j in range(0, len(array)+2):
            if i == ele:
                continue
            else:
                array[[i],[j]]=array[[i],[j]]-multi*array[[ele],[j]]
            
                
                 
    print()
    print(array)
    check(array)
        





#Wahl des Pivotelements
def pivotElement(array, stelle):
    mini = array[[0],[len(array)+1]]/array[[0],[stelle]]
    ele = 0
    for i in range(1,y-1):
        #print(str(array[[i],[len(array)+1]]/array[[i],[stelle]]))
        if array[[i],[stelle]]!=0 and ((array[[i], [len(array) + 1]] / array[[i], [stelle]]) < mini):
        #if ((array[[i],[len(array)+1]]/array[[i],[stelle]]) < mini):
            mini =  array[[i],[len(array)+1]]/array[[i],[stelle]]

            ele = i
            #print("Mini:" +str(mini))
    #print("Spalte: "+str(stelle)+"   Zeile: "+str(ele))
    #Übergabe an SImplex
    simplex(array,ele,stelle)


#Wahl der Pivotspalte
def pivotSpalte(array):
     #Pivot Spalte bestimmen
    stelle = 0
    mini = 0
    for i in range(0,len(array)-1):
        if array[[y-1],[i]]>array[[y-1],[i+1]]:
            mini = array[[y-1],[i+1]]
            stelle = i+1
    #Aufruf pivotElement
    pivotElement(array,stelle)


#else überarbeiten
def check(array):
    #überprüfen ob optimale Lösung gefunden
    test = False
    for i in range(0,len(array)-1):
        if array[[y-1],[i]]<0:
            test = True
            pivotSpalte(array)
        
    if test == False:
        print("optimale Lösung gefunden")
        print(array)



#Umformungsmethode, mit 0 auffüllen und Z Funktion bei Max *-1
#umformen = hinzufügen von 0 für die Schlupfvariablen
def transform(array):
    array2=numpy.zeros((y,x+y-1))
    for i in range(0, y):
        for j in range (0, x):
            if j == x-1:
                array2[[i],[x+y-2]] = array[[i],[x-1]]
            else:
                array2[[i],[j]]=array[[i],[j]]
    

    a = x-1
    b = 0
    #Schlupfvariablen 1 zuweisen
    for e in range (0, y-1):
        array2[[b],[a]] = 1
        b = b+1
        a= a+1

    
    #Zielfunktionszeile *-1 nehmen falls Max Funktion (1 für b in Zf)
    if array2[[y-1],[x+y-2]]==1:
        for d in range (0, x+y-2):
            array2[[y-1],[d]]=array2[[y-1],[d]]*-1
    array2[[y-1],[x+y-2]]=0
    array=array2
    print(array)
    #Aufruf Simplex

    check(array)


#Array befüllen mit Zahlen (Interaktion mit Anwender)
def arrayFill():
    for i in range (0, y) :    
        for j in range (0,x-1):
            #if für Zielfunktion, da anderer Text
            if i == (y-1):
                string = ("Geben Sie die " + str(j+1) + ". Strukturvariable der Zielfunktion an: ")
                platzhalter = input(string)
                array[[i],[j]] = int(platzhalter)
            else:

                string = ("Geben Sie die " + str(j+1) + ". Strukturvariable der " + str(i+1) +". Nebenbedingung an: ")

                platzhalter=input(string)

                array[[i],[j]] = int(platzhalter)
        #b eingeben
        print("Geben Sie bei der Zf für Max 1 ein und für Min 0")
        string = ("Geben Sie b der "+ str(i+1) + ". Nebenbedingung an: ")
        platzhalter = input(string)
        array[[i],[j+1]] = int(platzhalter)
        #print(array)


    #Übergabe an Umformungsmethode
    transform(array) 

#Methodenaufruf zum Starten des Programms
#########################################################
#arrayFill()
transform(array3)
########################################################
