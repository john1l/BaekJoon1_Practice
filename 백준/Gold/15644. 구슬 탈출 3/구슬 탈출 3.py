from collections import deque 
import sys 
input = sys.stdin.readline
from collections import defaultdict 

R, C = map(int, input().split())
mat = [ input() for _ in range(R) ] 


for r in range(R):
    for c in range(C):
        if mat[r][c] in ['R','B']:
            if mat[r][c]=='R': 
                rx ,ry = r,c 
            else: 
                bx , by = r,c 
       

dir4 = { 'U':[-1,0] , 'R':[0,1] , 'D':[1,0] , 'L':[0,-1] }
dic = defaultdict(int)
for k,v in dir4.items():
    dic[(v[0],v[1])] = k

def incline(x,y,a,b):
    cnt = 0
    while mat[x+a][y+b] !='#' and mat[x][y] !='O':
        x +=a ; y +=b ; cnt +=1
    return x ,y, cnt

visit = [[[ [0]*C for _ in range(R) ] for _ in range(C) ]  for _ in range(R) ]

q =deque()
s = '' 
q.append([rx,ry,bx,by,1,s])
visit[rx][ry][bx][by] = 1
def simul():

    while q:
        rx,ry,bx,by,dep ,s = q.popleft()
        
        if dep >10:
            print(-1) 
            return 

        for a,b in [(1,0),(-1,0),(0,1),(0,-1)]:

            nrx,nry ,rcnt  = incline(rx,ry,a,b)
            nbx ,nby , bcnt = incline(bx,by,a,b)

            if mat[nbx][nby] == 'O':
                continue
            if mat[nrx][nry] =='O':
                print(dep)
                print(s+dic[(a,b)]) 
                return

            if [nrx,nry] == [nbx,nby]:
                if rcnt < bcnt:
                    nbx -=a ; nby -=b
                else:
                    nrx -=a ; nry -=b

            if not visit[nrx][nry][nbx][nby]:

                visit[nrx][nry][nbx][nby] =1
                q.append( [nrx,nry,nbx,nby,dep+1, s+dic[(a,b)] ] )

    print(-1) 

simul()