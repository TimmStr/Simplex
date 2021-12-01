import numpy


x = int(input('Wie viele Strukturvariablen hat die Aufgabenstellung: '))+1
y = int(input('Wie viele Nebenbedingungen hat die Aufgabenstellung: '))+1
#x+1 für b                   y+1 für Zielfunktion
array=numpy.zeros((y,x))
print(array)

for i in range (0, y) :    
    for j in range (0,x-1):
        print("i"+str(i))
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
    string = ("Geben Sie b der "+ str(i+1) + ". Nebenbedingung an: ")
    platzhalter = input(string)
    array[[i],[j+1]] = int(platzhalter)
    print(array)
    

for a in range (0, x):
    string = ("Geben Sie die " + str(j+1) + ". Strukturvariable der Zielfunktion an: ")
