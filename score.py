eve=0
od=0
flag=0
k=0
li  = list(map(int,input().split(' ')))
print(li)
i=0
while i < len(li) :
        if li[i]%2 == 0 and flag == 1 :
            eve+=li[i]
            k=i+1 
            while k < len(li) and li[k]%2 != 0 :
                eve+=li[k]
                k+=1
            i=k-1
            flag=0
        else:
            od+=li[i]
            flag=1
            
        i+=1

print("p1:",od,"p2:",eve)
