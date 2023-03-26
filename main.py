import utils
import random
import time
import numpy as np
matrix= utils.generateMaze()
restartMaze=np.copy(matrix)
class No:
    filhos=None
    def __init__(self,i,j):
        self.filhos=[]
        self.pos=[i,j]
    def append(self,l):
        for ele in l:  
            self.filhos.append(No(ele[0],ele[1]))
    

compass=[[-1,0],[0,1],[+1,0],[0,-1]]

def sucessor(pos):
    random.shuffle(compass)
    directions=[[pos[0]+compass[0][0],pos[1]+compass[0][1]],[pos[0]+compass[1][0],pos[1]+compass[1][1]],[pos[0]+compass[2][0],pos[1]+compass[2][1]],[pos[0]+compass[3][0],pos[1]+compass[3][1]]]
    possibleMoves=[]
    for d in directions:
        if d[0]>=0 and d[0]<utils.n and d[1]>=0 and d[1]<utils.n:
            if matrix[d[0]][d[1]] == 1 or matrix[d[0]][d[1]]==3: 
                possibleMoves.append(d)
    return possibleMoves

def testeObjetivo(pos):
    return matrix[pos[0]][pos[1]] == 3

#dfs

def choseRandom(list):
    return list[random.randint(0,len(list)-1)]

def BFS():
    global matrix
    atuais = [No(0,0)]
    auxAtuais = []
    arrived=False
    step=4
    matrixInicial = np.copy(matrix)
    while not arrived:
        utils.UIupdate(matrix)
        for no in (atuais):
            no.append(sucessor(no.pos))
            for i in range(len(no.filhos)):
                auxAtuais.append(no.filhos[i])

            matrix[no.pos[0]][no.pos[1]] = step
        atuais = auxAtuais
        auxAtuais = []
        for no in atuais:
            if testeObjetivo(no.pos)==True:
                arrived=True
                posX=no.pos[0]
                posY=no.pos[1]
                lastNum=step
                while(lastNum>4):
                    directions=[[posX-1,posY],[posX,posY+1],[posX+1,posY],[posX,posY-1]]
                    for d in directions:
                        if d[0]>=0 and d[0]<utils.n and d[1]>=0 and d[1]<utils.n:
                            if matrix[d[0]][d[1]] == lastNum:
                                matrixInicial[d[0]][d[1]]=4
                                posX=d[0]
                                posY=d[1]
                                lastNum-=1
                                break 
                matrix=matrixInicial
                break
            matrix[no.pos[0]][no.pos[1]] = 2
        step+=1
        time.sleep(0.1)
        
        
def DFS():
    global matrix       
    atual = No(0,0)
    aux=None
    pilhaRamificacao=[]

    while True:
        utils.UIupdate(matrix)
        possibleMoves=sucessor(atual.pos)
        if(len(possibleMoves)>1):
            pilhaRamificacao.append([atual,np.copy(matrix)]) 
        if(len(possibleMoves)==0):
            while(len(pilhaRamificacao[-1][0].filhos)==0):
                pilhaRamificacao.pop()
            matrix=np.copy(pilhaRamificacao[-1][1])
            atual=pilhaRamificacao[-1][0]
            utils.UIupdate(matrix)
        matrix[atual.pos[0]][atual.pos[1]]=4
        atual.append(possibleMoves)
        aux=atual
        atual = atual.filhos[-1]
        aux.filhos.pop()
        if testeObjetivo(atual.pos)==True:     break
        matrix[atual.pos[0]][atual.pos[1]]=2
        time.sleep(0.01)
print("começando BFS")
BFS()
utils.UIupdate(matrix)
matrix=restartMaze
time.sleep(5)
utils.UIupdate(matrix)
print("começando DFS")
DFS()
while True:
    utils.UIupdate(matrix)
