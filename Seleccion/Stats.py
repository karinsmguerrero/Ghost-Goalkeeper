stats=open("StatsTeams.txt","r+")



def readstats():
    stats.seek(0)
    Lista= stats.readline()
    Fila=0
    StatList=[]    

    while Fila<3:
        StatList.append([])

        while len(StatList[Fila])<9:
            for i in Lista:
                if i!="," and len(StatList[Fila])<9:
                    StatList[Fila].append(int(i))
                    
        Fila+=1
            
        

    
    return StatList


def statslist():
    stats.seek(0)

    Lista= stats.readline()

    StatList=[[]]

    Fila=0

    palabra=""

    
    for i in Lista:

        if Fila>2:
            return StatList

            
        elif len(StatList[Fila])<8:
            if i!=",":
                palabra+=i

            elif i==",":
                StatList[Fila].append(int(palabra))
                palabra=""
        elif len(StatList[Fila])==8:
            Fila+=1
            if Fila>2:
                return StatList
            else:
                StatList.append([])
                if i!=",":
                    palabra+=i

                elif i==",":
                    StatList[Fila].append(int(palabra))
                    palabra=""
    
                
        
        
            

    return StatList



def clear():
    clearer=""
    stats.seek(0)
    for i in str(statslist()):
        clearer+=" "
    
    stats.seek(0)
    
    stats.write(clearer)

    stats.seek(0)
    
    stats.write("0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,")

    stats.seek(0)

    return statslist()


def adding(fil,col):

    List=statslist()

    List[fil][col]+=1

    stats.seek(0)

    List=breaking(List)

    stats.write(List)

    return statslist()


def breaking(Mat):

    Writable=""

    for fil in Mat:
        for col in fil:
            Writable+=str(col)
            Writable+=","

    return Writable

def close():
    stats.close()

def showstat(fil,col):

    List=statslist()
    
    return List[fil][col]
    
        

    


    
