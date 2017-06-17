import random



def KN1():
    Lista=[0,1,2,3,4,5]

    Eleccion= random.choice(Lista)

    Continua= random.choice([-1,1])

    if Eleccion==0:
        Continua= Eleccion+1

        return (Eleccion,Continua)

    elif Eleccion==5:
        Continua= Eleccion-1

        return (Eleccion, Continua)

    else:

        Continua= Eleccion+Continua

        return (Eleccion,Continua)

def KN2():
    Lista=[0,1,2,3,4,5]

    Eleccion= random.choice(Lista)

    Continua1= random.choice([-1,1])
    Continua2= random.choice([-1,1])
    
    

    if Eleccion==0:
        Continua1= Eleccion+1
        Continua2= Continua1+1

        return (Eleccion,Continua1,Continua2)

    elif Eleccion==5:
        Continua1= Eleccion-1
        Continua2= Continua1-1

        return (Eleccion, Continua1, Continua2)

    else:

        
        if Continua1==Continua2:
            Continua2= Eleccion-Continua2
            Continua1= Eleccion+Continua1
        else:
            Continua2= Eleccion+Continua2
            Continua1= Eleccion+Continua1

        return (Eleccion,Continua1, Continua2)


def KN3():
    Lista=[0,1,2,3,4,5]


    Eleccion=random.choice([0,1])

    return (Eleccion, Eleccion+2, Eleccion+4)


def rand_ind():
    Ele=random.choice([0,1,2])


    if Ele==0:
        return KN1()
    elif Ele==1:
        return KN2()
    else:
        return KN3()

def atajar(ele):

    port=rand_ind()

    lim= len(port)

    for i in port:
        if ele==i:
            
            return False


    
    return True







    

    
    
    
