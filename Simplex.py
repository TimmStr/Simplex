nb1 =[16,6,1,0,252]
nb2 =[4,12,0,1,168]
zf=[150,100,0,0,0,1]
z=[]
#1 für Max
if zf[len(zf)-1==1]:
    z=[i*-1 for i in zf]
    z.pop()
    
   
    
print(nb1)
print(nb2)
print(z)
print("")


def rechnePivotE(stelle):
    min1=nb1[len(nb1)-1]/nb1[stelle]
    min2=nb2[len(nb2)-1]/nb2[stelle]
    if min1 < min2 and min1 >0 or min2==0:

    #if min1 < min2 and min1 >0:
        teiler=nb1[stelle]
        for i in range(0,len(nb1)):
            nb1[i]=nb1[i]/teiler
            i=i+1
        
        
        teilernb2 = nb2[stelle]/nb1[stelle]
        if(teilernb2 >0 and nb2[stelle]>0)or(teilernb2<0 and nb2[stelle]<0) and teilernb2>0:    
            for i in range(0,len(nb1)):
                nb2[i]=nb2[i]-teilernb2*nb1[i]
        elif(teilernb2<0 and nb2[stelle]>0)or(teilernb2>0 and nb2[stelle]<0):
            for i in range(0,len(nb1)):
                nb2[i]=nb2[i]+teilernb2*nb1[i]  
            
            
        teilerz = z[stelle]/nb1[stelle]  
        if(teilerz >0 and z[stelle]>0)or(teilerz<0 and z[stelle]<0): 
            i=0
            for i in range(0,len(nb1)):
                z[i]=z[i]-teilerz*nb1[i]
                i=i+1
        elif(teilerz<0 and z[stelle]>0)or(teilerz>0 and z[stelle]<0):
            for i in range(0,len(nb1)):
                z[i]=z[i]+teilerz*nb1[i]  
        print(nb1)
        print(nb2)
        print(z)
        print("")
        #bis hierhin läuft der Aal
        if min1 > min2 and min2 >0:
            teiler=nb2[stelle]
            i=0
            for i in range(0,len(nb2)):
                nb2[i]=nb2[i]/teiler
                i=i+1
        
        




        if(teilernb1 >0 and nb1[stelle]>0)or(teilernb1<0 and nb1[stelle]<0):    
            for i in range(0,len(nb1)):
                nb2[i]=nb1[i]-teilernb2*nb2[i]
        elif(teilernb1<0 and nb1[stelle]>0)or(teilernb1>0 and nb1[stelle]<0):
            for i in range(0,len(nb1)):
                nb1[i]=nb1[i]+teilernb1*nb2[i]  
            
            
        teilerz = z[stelle]/nb2[stelle]  
        if(teilerz >0 and z[stelle]>0)or(teilerz<0 and z[stelle]<0): 
            i=0
            for i in range(0,len(nb2)):
                z[i]=z[i]-teilerz*nb2[i]
                i=i+1
        elif(teilerz<0 and z[stelle]>0)or(teilerz>0 and z[stelle]<0):
            for i in range(0,len(nb2)):
                z[i]=z[i]+teilerz*nb2[i]  
        print(nb1)
        print(nb2)
        print(z)
        
    b=True
    for i in range(0,len(z)):
        if(z[i]<0):
            b=False
    if(b==False):
        rechnePivotS(z)
    else:
        print("Lösung gefunden")
        print(nb1)
        print(nb2)
        print(z)



def rechnePivotS(zx):
    mini =z[0]
    stelle= 0
    for i in range(1,len(z)-1):
        if mini > zx[i]:
                mini = zx[i]
                stelle=i
    rechnePivotE(stelle)
    
rechnePivotS(z) 


