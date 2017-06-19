stats=open("StatsPlayers.txt","r+")




def player_stats():
    stats.seek(0)
    
    List=stats.readline()

    List=List.split(",")

    List=List[:-1]
    
    

    for i in range(0,len(List)):
        List[i]=int(List[i])


    Ind1=int(len(List)/3)
    
    Ind2=0

    Ind3=3

    Res1=[]    

    while Ind1>0:
        Counter=3
        Res1.append([])
        
        while Counter>0:

            Res1[-1].append(List[Ind2])

            Ind2+=1

            Counter-=1

        Ind1-=1
        

    return Mat1(Res1)

def Mat1(List):

    Ind=3

    Ind2=0

    Mat=[]
    
    while Ind:
        
        Mat.append([])

        Counter=7
    
        while Counter>0:
            Counter-=1
            
            Mat[-1].append(List[Ind2])
            
            Ind2+=1
        Ind-=1

    return Mat



def player_adding(Team,Player,Ind):
    Mat=player_stats()

    Mat[Team][Player][Ind]+=1

    rewrite(Mat)

    return player_stats()

def player_rewrite(List):

    rewritable=""

    for fil in List:
        for col in fil:
            for ele in col:

                rewritable+=str(ele)

                rewritable+=","

    stats.seek(0)

    stats.write(rewritable)

    stats.seek(0)
                
                

    return stats.readline()


def player_reset():

    List=player_stats()

    rewritable=""

    for fil in List:
        for col in fil:
            for ele in col:
                for i in range(0,len(str(ele))):

                    rewritable+=str(0)

                    rewritable+=","


    stats.seek(0)

    stats.write(rewritable)

    stats.seek(0)
                
                

    return player_stats()




    

        



    


