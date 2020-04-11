T = int(input())

for case in range(T):
    N = int(input())
    
    Matrix = []
    
    r = 0
    c = 0
    k = 0
    
    Col_Matrix = []
    

    for i in range(N):
        row = list(map(int,input().split()))
        Matrix.append(row)
        
        k += row[i]
        
        if N != len(set(row)):
            r += 1
        
        if i==0:
        
            for j in row:
                Col_Matrix.append([j])
                
        else:
            
            for j in range(N):
                Col_Matrix[j].append(row[j])
                
    
    for i in range(N):
        
        if N != len(set(Col_Matrix[i])):
            c += 1
            
    msg = "Case #"+str(case+1)+": "+str(k)+" "+str(r)+" "+str(c)
    print(msg)
            
            
            
        