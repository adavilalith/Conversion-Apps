def func(h,corals):
    water=0
    for i in corals:
        if h>i:
           water+=h-i
    return water


n=int(input())
for asf in range(n):
    temp=input().split()
    no=int(temp[0])
    x=int(temp[1])
    corals=input().split()
    corals=[int(i) for i in corals]
    low=0
    high=max(max(corals),x)
    c=0
    for i in range(high,0,-1):
        if func(i,corals)<=x:
            print(i)
            break
        
    
    